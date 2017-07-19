"""Test CWL workflow functionality."""
import json
import os
import re

from galaxy.util import galaxy_root_path

from .test_workflows import BaseWorkflowsApiTestCase

cwl_tool_directory = os.path.join(galaxy_root_path, "test", "functional", "tools", "cwl_tools")


class CwlWorkflowsTestCase(BaseWorkflowsApiTestCase):
    """Test case encompassing CWL workflow tests."""

    require_admin_user = True

    def test_simplest_wf(self):
        """Test simplest workflow."""
        load_response = self._load_workflow("v1.0_custom/just-wc-wf.cwl")
        self._assert_status_code_is(load_response, 200)
        workflow = load_response.json()
        workflow_id = workflow["id"]
        workflow_content = self._download_workflow(workflow_id)
        for step_index, step in workflow_content["steps"].items():
            if "tool_representation" in step:
                del step["tool_representation"]
        # AssertionError: Request status code (400) was not expected value 200. Body was {u'err_msg': u"Workflow cannot be run because an expected input step '1' has no input dataset.", u'err_code': 0}
        history_id = self.dataset_populator.new_history()
        hda1 = self.dataset_populator.new_dataset(history_id, content="hello world\nhello all\nhello all in world\nhello")
        inputs_map = {
            "file1": {"src": "hda", "id": hda1["id"]}
        }
        workflow_request = dict(
            history="hist_id=%s" % history_id,
            workflow_id=workflow_id,
            inputs=json.dumps(inputs_map),
            inputs_by="name",
        )
        url = "workflows/%s/invocations" % workflow_id
        invocation_response = self._post(url, data=workflow_request)
        self._assert_status_code_is(invocation_response, 200)
        invocation_id = invocation_response.json()["id"]
        self.wait_for_invocation_and_jobs(history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(history_id, hid=2)
        assert re.search(r"\s+4\s+9\s+47\s+", output)

    def test_count_line1_v1(self):
        """Test simple workflow v1.0/count-lines1-wf.cwl."""
        self._run_count_lines_wf("v1.0/count-lines1-wf.cwl")

    def test_count_line1_draft3(self):
        """Test simple workflow draft3/count-lines1-wf.cwl."""
        self._run_count_lines_wf("draft3/count-lines1-wf.cwl")

    def test_count_line2_v1(self):
        """Test simple workflow v1.0/count-lines2-wf.cwl."""
        self._run_count_lines_wf("v1.0/count-lines2-wf.cwl")

    def test_count_lines3_v1(self):
        load_response = self._load_workflow("v1.0/count-lines3-wf.cwl")
        self._assert_status_code_is(load_response, 200)
        workflow = load_response.json()
        workflow_id = workflow["id"]
        history_id = self.dataset_populator.new_history()
        hdca = self.dataset_collection_populator.create_list_in_history( history_id ).json()
        inputs_map = {
            "file1": {"src": "hdca", "id": hdca["id"]}
        }
        workflow_request = dict(
            history="hist_id=%s" % history_id,
            workflow_id=workflow_id,
            inputs=json.dumps(inputs_map),
            inputs_by="name",
        )
        url = "workflows/%s/invocations" % workflow_id
        invocation_response = self._post(url, data=workflow_request)
        self._assert_status_code_is(invocation_response, 200)
        invocation_id = invocation_response.json()["id"]
        self.wait_for_invocation_and_jobs(history_id, workflow_id, invocation_id)
        hdca = self.dataset_populator.get_history_collection_details(history_id, hid=8)
        assert hdca["collection_type"] == "list"
        elements = hdca["elements"]
        assert len(elements) == 3
        element0 = elements[0]["object"]
        assert element0["history_content_type"] == "dataset"
        assert element0["state"] == "ok"
        assert element0["file_ext"] == "expression.json"

    def _run_count_lines_wf(self, wf_path):
        load_response = self._load_workflow(wf_path)
        self._assert_status_code_is(load_response, 200)
        workflow = load_response.json()
        workflow_id = workflow["id"]
        history_id = self.dataset_populator.new_history()
        hda1 = self.dataset_populator.new_dataset(history_id, content="hello world\nhello all\nhello all in world\nhello")
        inputs_map = {
            "file1": {"src": "hda", "id": hda1["id"]}
        }
        workflow_request = dict(
            history="hist_id=%s" % history_id,
            workflow_id=workflow_id,
            inputs=json.dumps(inputs_map),
            inputs_by="name",
        )
        url = "workflows/%s/invocations" % workflow_id
        invocation_response = self._post(url, data=workflow_request)
        self._assert_status_code_is(invocation_response, 200)
        invocation_id = invocation_response.json()["id"]
        self.wait_for_invocation_and_jobs(history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(history_id, hid=2)
        assert re.search(r"\s+4", output)

    def _load_workflow(self, rel_path):
        path = os.path.join(cwl_tool_directory, rel_path)
        data = dict(
            from_path=path,
        )
        route = "workflows"
        upload_response = self._post(route, data=data)
        return upload_response
