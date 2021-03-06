import os

from galaxy import (
    exceptions,
    web
)
from galaxy.managers.context import ProvidesAppContext
from galaxy.web import (
    expose_api,
    expose_api_raw
)
from galaxy.webapps.base.controller import BaseAPIController


class ToolData(BaseAPIController):
    """
    RESTful controller for interactions with tool data
    """

    @web.require_admin
    @expose_api
    def index(self, trans: ProvidesAppContext, **kwds):
        """
        GET /api/tool_data

        Return a list tool_data tables.
        """
        return list(a.to_dict() for a in self._data_tables.values())

    @web.require_admin
    @expose_api
    def show(self, trans: ProvidesAppContext, id, **kwds):
        return self._data_table(id).to_dict(view='element')

    @web.require_admin
    @expose_api
    def reload(self, trans, id, **kwd):
        """
        GET /api/tool_data/{id}/reload

        Reloads a tool_data table.
        """
        decoded_tool_data_id = id
        data_table = self.app.tool_data_tables.data_tables.get(decoded_tool_data_id)
        data_table.reload_from_files()
        self.app.queue_worker.send_control_task(
            'reload_tool_data_tables',
            noop_self=True,
            kwargs={'table_name': decoded_tool_data_id}
        )
        return self._data_table(decoded_tool_data_id).to_dict(view='element')

    @web.require_admin
    @expose_api
    def delete(self, trans: ProvidesAppContext, id, **kwd):
        """
        DELETE /api/tool_data/{id}
        Removes an item from a data table

        :type   id:     str
        :param  id:     the id of the data table containing the item to delete
        :type   kwd:    dict
        :param  kwd:    (required) dictionary structure containing:

            * payload:     a dictionary itself containing:
                * values:   <TAB> separated list of column contents, there must be a value for all the columns of the data table
        """
        decoded_tool_data_id = id

        try:
            data_table = self.app.tool_data_tables.data_tables.get(decoded_tool_data_id)
        except Exception:
            data_table = None
        if not data_table:
            raise exceptions.RequestParameterInvalidException("Invalid data table id ( %s ) specified." % str(decoded_tool_data_id))

        values = None
        if kwd.get('payload', None):
            values = kwd['payload'].get('values', '')

        if not values:
            raise exceptions.RequestParameterInvalidException("Invalid data table item ( %s ) specified." % str(values))

        split_values = values.split("\t")

        if len(split_values) != len(data_table.get_column_name_list()):
            raise exceptions.RequestParameterInvalidException("Invalid data table item ( {} ) specified. Wrong number of columns ({} given, {} required).".format(str(values), str(len(split_values)), str(len(data_table.get_column_name_list()))))

        data_table.remove_entry(split_values)
        self.app.queue_worker.send_control_task(
            'reload_tool_data_tables',
            noop_self=True,
            kwargs={'table_name': decoded_tool_data_id}
        )
        return self._data_table(decoded_tool_data_id).to_dict(view='element')

    @web.require_admin
    @expose_api
    def show_field(self, trans: ProvidesAppContext, id, value, **kwds):
        """
        GET /api/tool_data/<id>/fields/<value>

        Get information about a partiular field in a tool_data table
        """
        return self._data_table_field(id, value).to_dict()

    @web.require_admin
    @expose_api_raw
    def download_field_file(self, trans: ProvidesAppContext, id: str, value, path, **kwds):
        field_value = self._data_table_field(id, value)
        base_dir = field_value.get_base_dir()
        full_path = os.path.join(base_dir, path)
        if full_path not in field_value.get_files():
            raise exceptions.ObjectNotFound("No such path in data table field.")
        return open(full_path, "rb")

    def _data_table_field(self, id, value):
        out = self._data_table(id).get_field(value)
        if out is None:
            raise exceptions.ObjectNotFound(f"No such field {value} in data table {id}.")
        return out

    def _data_table(self, id):
        try:
            return self._data_tables[id]
        except IndexError:
            raise exceptions.ObjectNotFound("No such data table %s" % id)

    @property
    def _data_tables(self):
        return self.app.tool_data_tables.data_tables
