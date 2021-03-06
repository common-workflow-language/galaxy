"""Test CWL conformance for version v1.1."""

import pytest

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version v1.1."""

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_cl_basic_generation(self):
        """General test of command line generation

        Generated from::

            id: 1
            job: tests/bwa-mem-job.json
            label: cl_basic_generation
            output:
              args:
              - bwa
              - mem
              - -t
              - '2'
              - -I
              - 1,2,3,4
              - -m
              - '3'
              - chr20.fa
              - example_human_Illumina.pe_1.fastq
              - example_human_Illumina.pe_2.fastq
            tags:
            - required
            - command_line_tool
            tool: tests/bwa-mem-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """General test of command line generation""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_nested_prefixes_arrays(self):
        """Test nested prefixes with arrays

        Generated from::

            id: 2
            job: tests/bwa-mem-job.json
            label: nested_prefixes_arrays
            output:
              args:
              - bwa
              - mem
              - chr20.fa
              - -XXX
              - -YYY
              - example_human_Illumina.pe_1.fastq
              - -YYY
              - example_human_Illumina.pe_2.fastq
            tags:
            - required
            - command_line_tool
            tool: tests/binding-test.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested prefixes with arrays""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.schema_def
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_nested_cl_bindings(self):
        """Test nested command line bindings

        Generated from::

            id: 3
            job: tests/tmap-job.json
            label: nested_cl_bindings
            output:
              args:
              - tmap
              - mapall
              - stage1
              - map1
              - --min-seq-length
              - '20'
              - map2
              - --min-seq-length
              - '20'
              - stage2
              - map1
              - --max-seq-length
              - '20'
              - --min-seq-length
              - '10'
              - --seed-length
              - '16'
              - map2
              - --max-seed-hits
              - '-1'
              - --max-seq-length
              - '20'
              - --min-seq-length
              - '10'
            tags:
            - schema_def
            - command_line_tool
            tool: tests/tmap-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested command line bindings""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_cl_optional_inputs_missing(self):
        """Test command line with optional input (missing)

        Generated from::

            id: 4
            job: tests/cat-job.json
            label: cl_optional_inputs_missing
            output:
              args:
              - cat
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: tests/cat1-testcli.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with optional input (missing)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_cl_optional_bindings_provided(self):
        """Test command line with optional input (provided)

        Generated from::

            id: 5
            job: tests/cat-n-job.json
            label: cl_optional_bindings_provided
            output:
              args:
              - cat
              - -n
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: tests/cat1-testcli.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with optional input (provided)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initworkdir_expreng_requirements(self):
        """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature

        Generated from::

            id: 6
            job: tests/cat-job.json
            label: initworkdir_expreng_requirements
            output:
              foo:
                checksum: sha1$63da67422622fbf9251a046d7a34b7ea0fd4fead
                class: File
                location: foo.txt
                size: 22
            tags:
            - initial_work_dir
            - inline_javascript
            - command_line_tool
            tool: tests/template-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stdout_redirect_docker(self):
        """Test command execution in Docker with stdout redirection

        Generated from::

            id: 7
            job: tests/cat-job.json
            label: stdout_redirect_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with stdout redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stdout_redirect_shortcut_docker(self):
        """Test command execution in Docker with shortcut stdout redirection

        Generated from::

            id: 8
            job: tests/cat-job.json
            label: stdout_redirect_shortcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: Any
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool-shortcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with shortcut stdout redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stdout_redirect_mediumcut_docker(self):
        """Test command execution in Docker with mediumcut stdout redirection

        Generated from::

            id: 9
            job: tests/cat-job.json
            label: stdout_redirect_mediumcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: cat-out
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool-mediumcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with mediumcut stdout redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stderr_redirect(self):
        """Test command line with stderr redirection

        Generated from::

            id: 10
            job: tests/empty.json
            label: stderr_redirect
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: error.txt
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: tests/stderr.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stderr_redirect_shortcut(self):
        """Test command line with stderr redirection, brief syntax

        Generated from::

            id: 11
            job: tests/empty.json
            label: stderr_redirect_shortcut
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: Any
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: tests/stderr-shortcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection, brief syntax""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stderr_redirect_mediumcut(self):
        """Test command line with stderr redirection, named brief syntax

        Generated from::

            id: 12
            job: tests/empty.json
            label: stderr_redirect_mediumcut
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: std.err
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: tests/stderr-mediumcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection, named brief syntax""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stdinout_redirect_docker(self):
        """Test command execution in Docker with stdin and stdout redirection

        Generated from::

            id: 13
            job: tests/cat-job.json
            label: stdinout_redirect_docker
            output:
              output_txt:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - required
            - command_line_tool
            tool: tests/cat4-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with stdin and stdout redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any(self):
        """Test default usage of Any in expressions.

        Generated from::

            id: 14
            job: tests/empty.json
            label: expression_any
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default usage of Any in expressions.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any_null(self):
        """Test explicitly passing null to Any type inputs with default values.

        Generated from::

            id: 15
            job: tests/null-expression1-job.json
            label: expression_any_null
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test explicitly passing null to Any type inputs with default values.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any_string(self):
        """Testing the string 'null' does not trip up an Any with a default value.

        Generated from::

            id: 16
            job: tests/null-expression2-job.json
            label: expression_any_string
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing the string 'null' does not trip up an Any with a default value.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any_nodefaultany(self):
        """Test Any without defaults cannot be unspecified.

        Generated from::

            id: 17
            job: tests/empty.json
            label: expression_any_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults cannot be unspecified.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any_null_nodefaultany(self):
        """Test explicitly passing null to Any type without a default value.

        Generated from::

            id: 18
            job: tests/null-expression1-job.json
            label: expression_any_null_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test explicitly passing null to Any type without a default value.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_any_nullstring_nodefaultany(self):
        """Testing the string 'null' does not trip up an Any without a default value.

        Generated from::

            id: 19
            job: tests/null-expression2-job.json
            label: expression_any_nullstring_nodefaultany
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing the string 'null' does not trip up an Any without a default value.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_any_outputSource_compatibility(self):
        """Testing Any type compatibility in outputSource

        Generated from::

            id: 20
            job: tests/any-type-job.json
            label: any_outputSource_compatibility
            output:
              output1:
              - hello
              - world
              output2:
              - foo
              - bar
              output3: hello
            tags:
            - required
            - workflow
            tool: tests/any-type-compat.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing Any type compatibility in outputSource""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_stdinout_redirect(self):
        """Test command execution in with stdin and stdout redirection

        Generated from::

            id: 21
            job: tests/cat-job.json
            label: stdinout_redirect
            output:
              output:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output
                size: 13
            tags:
            - required
            - command_line_tool
            tool: tests/cat-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in with stdin and stdout redirection""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_parseint(self):
        """Test ExpressionTool with Javascript engine

        Generated from::

            id: 22
            job: tests/parseInt-job.json
            label: expression_parseint
            output:
              output: 42
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/parseInt-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test ExpressionTool with Javascript engine""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_expression_outputEval(self):
        """Test outputEval to transform output

        Generated from::

            id: 23
            job: tests/wc-job.json
            label: expression_outputEval
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/wc2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test outputEval to transform output""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_parseInt(self):
        """Test two step workflow with imported tools

        Generated from::

            id: 24
            job: tests/wc-job.json
            label: wf_wc_parseInt
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines1-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test two step workflow with imported tools""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_expressiontool(self):
        """Test two step workflow with inline tools

        Generated from::

            id: 25
            job: tests/wc-job.json
            label: wf_wc_expressiontool
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines2-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test two step workflow with inline tools""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_scatter(self):
        """Test single step workflow with Scatter step

        Generated from::

            id: 26
            job: tests/count-lines3-job.json
            label: wf_wc_scatter
            output:
              count_output:
              - 16
              - 1
            tags:
            - scatter
            - inline_javascript
            - workflow
            tool: tests/count-lines3-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test single step workflow with Scatter step""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.multiple_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_scatter_multiple_merge(self):
        """Test single step workflow with Scatter step and two data links connected to same input, default merge behavior

        Generated from::

            id: 27
            job: tests/count-lines4-job.json
            label: wf_wc_scatter_multiple_merge
            output:
              count_output:
              - 16
              - 1
            tags:
            - scatter
            - multiple_input
            - inline_javascript
            - workflow
            tool: tests/count-lines4-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test single step workflow with Scatter step and two data links connected to same input, default merge behavior""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.multiple_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_wc_scatter_multiple_nested(self):
        """Test single step workflow with Scatter step and two data links connected to same input, nested merge behavior

        Generated from::

            id: 28
            job: tests/count-lines6-job.json
            label: wf_wc_scatter_multiple_nested
            output:
              count_output:
              - 32
              - 2
            tags:
            - scatter
            - multiple_input
            - inline_javascript
            - workflow
            tool: tests/count-lines6-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test single step workflow with Scatter step and two data links connected to same input, nested merge behavior""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.multiple_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_scatter_multiple_flattened(self):
        """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior

        Generated from::

            id: 29
            job: tests/count-lines6-job.json
            label: wf_wc_scatter_multiple_flattened
            output:
              count_output: 34
            tags:
            - multiple_input
            - inline_javascript
            - workflow
            tool: tests/count-lines7-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_wc_nomultiple(self):
        """Test that no MultipleInputFeatureRequirement is necessary when workflow step source is a single-item list

        Generated from::

            id: 30
            job: tests/count-lines6-job.json
            label: wf_wc_nomultiple
            output:
              count_output: 32
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines13-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that no MultipleInputFeatureRequirement is necessary when workflow step source is a single-item list""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_input_default_missing(self):
        """Test workflow with default value for input parameter (missing)

        Generated from::

            id: 31
            job: tests/empty.json
            label: wf_input_default_missing
            output:
              count_output: 1
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines5-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow with default value for input parameter (missing)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_input_default_provided(self):
        """Test workflow with default value for input parameter (provided)

        Generated from::

            id: 32
            job: tests/wc-job.json
            label: wf_input_default_provided
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines5-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow with default value for input parameter (provided)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_default_tool_default(self):
        """Test that workflow defaults override tool defaults

        Generated from::

            id: 33
            job: tests/empty.json
            label: wf_default_tool_default
            output:
              default_output: workflow_default
            tags:
            - required
            - workflow
            tool: tests/echo-wf-default.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that workflow defaults override tool defaults""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.env_var
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_envvar_req(self):
        """Test EnvVarRequirement

        Generated from::

            id: 34
            job: tests/env-job.json
            label: envvar_req
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - env_var
            - command_line_tool
            tool: tests/env-tool1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test EnvVarRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_single_param(self):
        """Test workflow scatter with single scatter parameter

        Generated from::

            id: 35
            job: tests/scatter-job1.json
            label: wf_scatter_single_param
            output:
              out:
              - foo one
              - foo two
              - foo three
              - foo four
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with single scatter parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_two_nested_crossproduct(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method

        Generated from::

            id: 36
            job: tests/scatter-job2.json
            label: wf_scatter_two_nested_crossproduct
            output:
              out:
              - - foo one three
                - foo one four
              - - foo two three
                - foo two four
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_two_flat_crossproduct(self):
        """Test workflow scatter with two scatter parameters and flat_crossproduct join method

        Generated from::

            id: 37
            job: tests/scatter-job2.json
            label: wf_scatter_two_flat_crossproduct
            output:
              out:
              - foo one three
              - foo one four
              - foo two three
              - foo two four
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf3.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and flat_crossproduct join method""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_two_dotproduct(self):
        """Test workflow scatter with two scatter parameters and dotproduct join method

        Generated from::

            id: 38
            job: tests/scatter-job2.json
            label: wf_scatter_two_dotproduct
            output:
              out:
              - foo one three
              - foo two four
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf4.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and dotproduct join method""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_scatter_emptylist(self):
        """Test workflow scatter with single empty list parameter

        Generated from::

            id: 39
            job: tests/scatter-empty-job1.json
            label: wf_scatter_emptylist
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with single empty list parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_nested_crossproduct_secondempty(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method with second list empty

        Generated from::

            id: 40
            job: tests/scatter-empty-job2.json
            label: wf_scatter_nested_crossproduct_secondempty
            output:
              out:
              - []
              - []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method with second list empty""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_nested_crossproduct_firstempty(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method with first list empty

        Generated from::

            id: 41
            job: tests/scatter-empty-job3.json
            label: wf_scatter_nested_crossproduct_firstempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf3.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method with first list empty""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_flat_crossproduct_oneempty(self):
        """Test workflow scatter with two scatter parameters, one of which is empty and flat_crossproduct join method

        Generated from::

            id: 42
            job: tests/scatter-empty-job2.json
            label: wf_scatter_flat_crossproduct_oneempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf3.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters, one of which is empty and flat_crossproduct join method""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_scatter_dotproduct_twoempty(self):
        """Test workflow scatter with two empty scatter parameters and dotproduct join method

        Generated from::

            id: 43
            job: tests/scatter-empty-job4.json
            label: wf_scatter_dotproduct_twoempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf4.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two empty scatter parameters and dotproduct join method""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_any_input_param(self):
        """Test Any type input parameter

        Generated from::

            id: 44
            job: tests/env-job.json
            label: any_input_param
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any type input parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.subworkflow
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_nested_workflow(self):
        """Test nested workflow

        Generated from::

            id: 45
            job: tests/wc-job.json
            label: nested_workflow
            output:
              count_output: 16
            tags:
            - subworkflow
            - workflow
            - inline_javascript
            tool: tests/count-lines8-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.env_var
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_requirement_priority(self):
        """Test requirement priority

        Generated from::

            id: 46
            job: tests/env-job.json
            label: requirement_priority
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - env_var
            - workflow
            tool: tests/env-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirement priority""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.env_var
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_requirement_override_hints(self):
        """Test requirements override hints

        Generated from::

            id: 47
            job: tests/env-job.json
            label: requirement_override_hints
            output:
              out:
                checksum: sha1$cdc1e84968261d6a7575b5305945471f8be199b6
                class: File
                location: out
                size: 9
            tags:
            - env_var
            - workflow
            tool: tests/env-wf2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirements override hints""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.env_var
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_requirement_workflow_steps(self):
        """Test requirements on workflow steps

        Generated from::

            id: 48
            job: tests/env-job.json
            label: requirement_workflow_steps
            output:
              out:
                checksum: sha1$cdc1e84968261d6a7575b5305945471f8be199b6
                class: File
                location: out
                size: 9
            tags:
            - env_var
            - workflow
            tool: tests/env-wf3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirements on workflow steps""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_step_input_default_value(self):
        """Test default value on step input parameter

        Generated from::

            id: 49
            job: tests/empty.json
            label: step_input_default_value
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines9-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_step_input_default_value_nosource(self):
        """Test use default value on step input parameter with empty source

        Generated from::

            id: 50
            job: tests/empty.json
            label: step_input_default_value_nosource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines11-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use default value on step input parameter with empty source""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_step_input_default_value_nullsource(self):
        """Test use default value on step input parameter with null source

        Generated from::

            id: 51
            job: tests/file1-null.json
            label: step_input_default_value_nullsource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines11-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use default value on step input parameter with null source""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden(self):
        """Test default value on step input parameter overridden by provided source

        Generated from::

            id: 52
            job: tests/cat-job.json
            label: step_input_default_value_overriden
            output:
              count_output: 1
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines11-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_simple(self):
        """Test simple workflow

        Generated from::

            id: 53
            job: tests/revsort-job.json
            label: wf_simple
            output:
              output:
                checksum: sha1$b9214658cc453331b62c2282b772a5c063dbd284
                class: File
                location: output.txt
                size: 1111
            tags:
            - required
            - workflow
            tool: tests/revsort.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_hints_unknown_ignored(self):
        """Test unknown hints are ignored.

        Generated from::

            id: 54
            job: tests/cat-job.json
            label: hints_unknown_ignored
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - required
            - command_line_tool
            tool: tests/cat5-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test unknown hints are ignored.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_secondary_files_expr(self):
        """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles on input and output. Also tests the use of a variety of parameter references and expressions in the secondaryFiles field.

        Generated from::

            id: 55
            job: tests/search-job.json
            label: initial_workdir_secondary_files_expr
            output:
              indexedfile:
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: input.txt
                secondaryFiles:
                - checksum: sha1$1f6fe811644355974cdd06d9eb695d6e859f3b44
                  class: File
                  location: input.txt.idx1
                  size: 1500
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.idx2
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx3
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx4
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx5
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.idx6.txt
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx7
                  size: 0
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
                - class: Directory
                  listing:
                  - basename: index
                    checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: index
                    size: 0
                  location: input.txt_idx8
                size: 1111
              outfile:
                checksum: sha1$e2dc9daaef945ac15f01c238ed2f1660f60909a0
                class: File
                location: result.txt
                size: 142
            tags:
            - initial_work_dir
            - inline_javascript
            - command_line_tool
            tool: tests/search.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles on input and output. Also tests the use of a variety of parameter references and expressions in the secondaryFiles field.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_rename(self):
        """Test InitialWorkDirRequirement with expression in filename.

        Generated from::

            id: 56
            job: tests/rename-job.json
            label: rename
            output:
              outfile:
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: fish.txt
                size: 1111
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/rename.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement with expression in filename.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_trailingnl(self):
        """Test if trailing newline is present in file entry in InitialWorkDir

        Generated from::

            id: 57
            job: tests/string-job.json
            label: initial_workdir_trailingnl
            output:
              out:
                checksum: sha1$6a47aa22b2a9d13a66a24b3ee5eaed95ce4753cf
                class: File
                location: example.conf
                size: 16
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/iwdr-entry.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test if trailing newline is present in file entry in InitialWorkDir""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_inline_expressions(self):
        """Test inline expressions

        Generated from::

            id: 58
            job: tests/wc-job.json
            label: inline_expressions
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/wc4-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test inline expressions""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.schema_def
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_schemadef_req_tool_param(self):
        """Test SchemaDefRequirement definition used in tool parameter

        Generated from::

            id: 59
            job: tests/schemadef-job.json
            label: schemadef_req_tool_param
            output:
              output:
                checksum: sha1$f12e6cfe70f3253f70b0dbde17c692e7fb0f1e5e
                class: File
                location: output.txt
                size: 12
            tags:
            - schema_def
            - command_line_tool
            tool: tests/schemadef-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test SchemaDefRequirement definition used in tool parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.schema_def
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_schemadef_req_wf_param(self):
        """Test SchemaDefRequirement definition used in workflow parameter

        Generated from::

            id: 60
            job: tests/schemadef-job.json
            label: schemadef_req_wf_param
            output:
              output:
                checksum: sha1$f12e6cfe70f3253f70b0dbde17c692e7fb0f1e5e
                class: File
                location: output.txt
                size: 12
            tags:
            - schema_def
            - workflow
            tool: tests/schemadef-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test SchemaDefRequirement definition used in workflow parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_param_evaluation_noexpr(self):
        """Test parameter evaluation, no support for JS expressions

        Generated from::

            id: 61
            job: tests/empty.json
            label: param_evaluation_noexpr
            output:
              t1:
                bar:
                  b az: 2
                  b"az: null
                  b'az: true
                  baz: zab1
                  buz:
                  - a
                  - b
                  - c
              t10: true
              t11: true
              t12: null
              t13: -zab1
              t14: -zab1
              t15: -zab1
              t16: -zab1
              t17: zab1 zab1
              t18: zab1 zab1
              t19: zab1 zab1
              t2:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t20: zab1 zab1
              t21: 2 2
              t22: true true
              t23: true true
              t24: null null
              t25: b
              t26: b b
              t27: null
              t28: 3
              t3:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t4:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t5: zab1
              t6: zab1
              t7: zab1
              t8: zab1
              t9: 2
            tags:
            - required
            - command_line_tool
            tool: tests/params.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test parameter evaluation, no support for JS expressions""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_param_evaluation_expr(self):
        """Test parameter evaluation, with support for JS expressions

        Generated from::

            id: 62
            job: tests/empty.json
            label: param_evaluation_expr
            output:
              t1:
                bar:
                  b az: 2
                  b"az: null
                  b'az: true
                  baz: zab1
                  buz:
                  - a
                  - b
                  - c
              t10: true
              t11: true
              t12: null
              t13: -zab1
              t14: -zab1
              t15: -zab1
              t16: -zab1
              t17: zab1 zab1
              t18: zab1 zab1
              t19: zab1 zab1
              t2:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t20: zab1 zab1
              t21: 2 2
              t22: true true
              t23: true true
              t24: null null
              t25: b
              t26: b b
              t27: null
              t28: 3
              t3:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t4:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t5: zab1
              t6: zab1
              t7: zab1
              t8: zab1
              t9: 2
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/params2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test parameter evaluation, with support for JS expressions""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_metadata(self):
        """Test metadata

        Generated from::

            id: 63
            job: tests/cat-job.json
            label: metadata
            output: {}
            tags:
            - required
            - command_line_tool
            tool: tests/metadata.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test metadata""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_format_checking(self):
        """Test simple format checking.

        Generated from::

            id: 64
            job: tests/formattest-job.json
            label: format_checking
            output:
              output:
                checksum: sha1$97fe1b50b4582cebc7d853796ebd62e3e163aa3f
                class: File
                format: http://edamontology.org/format_2330
                location: output.txt
                size: 1111
            tags:
            - required
            - command_line_tool
            tool: tests/formattest.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple format checking.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_format_checking_subclass(self):
        """Test format checking against ontology using subclassOf.

        Generated from::

            id: 65
            job: tests/formattest2-job.json
            label: format_checking_subclass
            output:
              output:
                checksum: sha1$971d88faeda85a796752ecf752b7e2e34f1337ce
                class: File
                format: http://edamontology.org/format_1929
                location: output.txt
                size: 12010
            tags:
            - required
            - command_line_tool
            tool: tests/formattest2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format checking against ontology using subclassOf.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_format_checking_equivalentclass(self):
        """Test format checking against ontology using equivalentClass.

        Generated from::

            id: 66
            job: tests/formattest2-job.json
            label: format_checking_equivalentclass
            output:
              output:
                checksum: sha1$971d88faeda85a796752ecf752b7e2e34f1337ce
                class: File
                format: http://edamontology.org/format_1929
                location: output.txt
                size: 12010
            tags:
            - required
            - command_line_tool
            tool: tests/formattest3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format checking against ontology using equivalentClass.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_output_secondaryfile_optional(self):
        """Test optional output file and optional secondaryFile on output.

        Generated from::

            id: 67
            job: tests/cat-job.json
            label: output_secondaryfile_optional
            output:
              optional_file: null
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/optional-output.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test optional output file and optional secondaryFile on output.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_valuefrom_ignored_null(self):
        """Test that valueFrom is ignored when the parameter is null

        Generated from::

            id: 68
            job: tests/empty.json
            label: valuefrom_ignored_null
            output:
              out: '
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/vf-concat.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that valueFrom is ignored when the parameter is null""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_valuefrom_secondexpr_ignored(self):
        """Test that second expression in concatenated valueFrom is not ignored

        Generated from::

            id: 69
            job: tests/cat-job.json
            label: valuefrom_secondexpr_ignored
            output:
              out: 'a string
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/vf-concat.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that second expression in concatenated valueFrom is not ignored""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_valuefrom_wf_step(self):
        """Test valueFrom on workflow step.

        Generated from::

            id: 70
            job: tests/step-valuefrom-wf.json
            label: valuefrom_wf_step
            output:
              count_output: 16
            tags:
            - step_input
            - inline_javascript
            - workflow
            tool: tests/step-valuefrom-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom on workflow step.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.multiple_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_valuefrom_wf_step_multiple(self):
        """Test valueFrom on workflow step with multiple sources

        Generated from::

            id: 71
            job: tests/step-valuefrom-job.json
            label: valuefrom_wf_step_multiple
            output:
              val: '3
            
                '
            tags:
            - step_input
            - inline_javascript
            - multiple_input
            - workflow
            tool: tests/step-valuefrom2-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom on workflow step with multiple sources""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_valuefrom_wf_step_other(self):
        """Test valueFrom on workflow step referencing other inputs

        Generated from::

            id: 72
            job: tests/step-valuefrom-job.json
            label: valuefrom_wf_step_other
            output:
              val: '3
            
                '
            tags:
            - step_input
            - inline_javascript
            - workflow
            tool: tests/step-valuefrom3-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom on workflow step referencing other inputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_record_output_binding(self):
        """Test record type output binding.

        Generated from::

            id: 73
            job: tests/record-output-job.json
            label: record_output_binding
            output:
              orec:
                obar:
                  checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                  class: File
                  location: bar
                  size: 12010
                ofoo:
                  checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: foo
                  size: 1111
            tags:
            - shell_command
            - command_line_tool
            tool: tests/record-output.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test record type output binding.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_docker_json_output_path(self):
        """Test support for reading cwl.output.json when running in a Docker container and just 'path' is provided.

        Generated from::

            id: 74
            job: tests/empty.json
            label: docker_json_output_path
            output:
              foo:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: foo
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: tests/test-cwl-out.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for reading cwl.output.json when running in a Docker container and just 'path' is provided.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_docker_json_output_location(self):
        """Test support for reading cwl.output.json when running in a Docker container and just 'location' is provided.

        Generated from::

            id: 75
            job: tests/empty.json
            label: docker_json_output_location
            output:
              foo:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: foo
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: tests/test-cwl-out2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for reading cwl.output.json when running in a Docker container and just 'location' is provided.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_multiple_glob_expr_list(self):
        """Test support for returning multiple glob patterns from expression

        Generated from::

            id: 76
            job: tests/abc.json
            label: multiple_glob_expr_list
            output:
              files:
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: a
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: b
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: c
                size: 0
            tags:
            - required
            - command_line_tool
            tool: tests/glob-expr-list.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for returning multiple glob patterns from expression""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_oneparam_valuefrom(self):
        """Test workflow scatter with single scatter parameter and two valueFrom on step input (first and current el)

        Generated from::

            id: 77
            job: tests/scatter-valuefrom-job1.json
            label: wf_scatter_oneparam_valuefrom
            output:
              out:
              - foo one one
              - foo one two
              - foo one three
              - foo one four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with single scatter parameter and two valueFrom on step input (first and current el)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_twoparam_nested_crossproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method and valueFrom on step input

        Generated from::

            id: 78
            job: tests/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_nested_crossproduct_valuefrom
            output:
              out:
              - - foo one one three
                - foo one one four
              - - foo one two three
                - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method and valueFrom on step input""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_twoparam_flat_crossproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and flat_crossproduct join method and valueFrom on step input

        Generated from::

            id: 79
            job: tests/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_flat_crossproduct_valuefrom
            output:
              out:
              - foo one one three
              - foo one one four
              - foo one two three
              - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf3.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and flat_crossproduct join method and valueFrom on step input""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_twoparam_dotproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and dotproduct join method and valueFrom on step input

        Generated from::

            id: 80
            job: tests/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_dotproduct_valuefrom
            output:
              out:
              - foo one one three
              - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf4.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with two scatter parameters and dotproduct join method and valueFrom on step input""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_oneparam_valuefrom_twice_current_el(self):
        """Test workflow scatter with single scatter parameter and two valueFrom on step input (current el twice)

        Generated from::

            id: 81
            job: tests/scatter-valuefrom-job1.json
            label: wf_scatter_oneparam_valuefrom_twice_current_el
            output:
              out:
              - foo one one
              - foo two two
              - foo three three
              - foo four four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf5.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with single scatter parameter and two valueFrom on step input (current el twice)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_oneparam_valueFrom(self):
        """Test valueFrom eval on scattered input parameter

        Generated from::

            id: 82
            job: tests/scatter-valuefrom-job3.json
            label: wf_scatter_oneparam_valueFrom
            output:
              out_message:
              - checksum: sha1$98030575f6fc40e5021be5a8803a6bef94aee11f
                class: File
                location: Any
                size: 16
              - checksum: sha1$edcacd50778d98ae113015406b3195c165059dd8
                class: File
                location: Any
                size: 16
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-wf6.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom eval on scattered input parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_two_inputfiles_namecollision(self):
        """Test workflow two input files with same name.

        Generated from::

            id: 83
            job: tests/conflict-job.json
            label: wf_two_inputfiles_namecollision
            output:
              fileout:
                checksum: sha1$a2d8d6e7b28295dc9977dc3bdb652ddd480995f0
                class: File
                location: out.txt
                size: 25
            tags:
            - required
            - workflow
            tool: tests/conflict-wf.cwl#collision
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow two input files with same name.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_directory_input_param_ref(self):
        """Test directory input with parameter reference

        Generated from::

            id: 84
            job: tests/dir-job.yml
            label: directory_input_param_ref
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: tests/dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory input with parameter reference""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.shell_command
    @pytest.mark.green
    def test_conformance_v1_1_directory_input_docker(self):
        """Test directory input in Docker

        Generated from::

            id: 85
            job: tests/dir-job.yml
            label: directory_input_docker
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - required
            - command_line_tool
            - shell_command
            tool: tests/dir2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory input in Docker""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_directory_output(self):
        """Test directory output

        Generated from::

            id: 86
            job: tests/dir3-job.yml
            label: directory_output
            output:
              outdir:
                class: Directory
                listing:
                - checksum: sha1$dd0a4c4c49ba43004d6611771972b6cf969c1c01
                  class: File
                  location: goodbye.txt
                  size: 24
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
            tags:
            - required
            - command_line_tool
            tool: tests/dir3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory output""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_directory_secondaryfiles(self):
        """Test directories in secondaryFiles

        Generated from::

            id: 87
            job: tests/dir4-job.yml
            label: directory_secondaryfiles
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: tests/dir4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directories in secondaryFiles""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_dynamic_initial_workdir(self):
        """Test dynamic initial work dir

        Generated from::

            id: 88
            job: tests/dir-job.yml
            label: dynamic_initial_workdir
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - initial_work_dir
            - command_line_tool
            tool: tests/dir5.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test dynamic initial work dir""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_writable_stagedfiles(self):
        """Test writable staged files.

        Generated from::

            id: 89
            job: tests/stagefile-job.yml
            label: writable_stagedfiles
            output:
              outfile:
                checksum: sha1$b769c7b2e316edd4b5eb2d24799b2c1f9d8c86e6
                class: File
                location: bob.txt
                size: 1111
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/stagefile.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test writable staged files.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_input_file_literal(self):
        """Test file literal as input

        Generated from::

            id: 90
            job: tests/file-literal.yml
            label: input_file_literal
            output:
              output_file:
                checksum: sha1$d0e04ff6c413c7d57f9a0ca0a33cd3ab52e2dd9c
                class: File
                location: output.txt
                size: 18
            tags:
            - required
            - command_line_tool
            tool: tests/cat3-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal as input""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_expr(self):
        """Test expression in InitialWorkDir listing

        Generated from::

            id: 91
            job: tests/arguments-job.yml
            label: initial_workdir_expr
            output:
              classfile:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Hello.class
                size: 0
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/linkfile.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test expression in InitialWorkDir listing""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_nameroot_nameext_stdout_expr(self):
        """Test nameroot/nameext expression in arguments, stdout

        Generated from::

            id: 92
            job: tests/wc-job.json
            label: nameroot_nameext_stdout_expr
            output:
              b:
                checksum: sha1$c4cfd130e7578714e3eef91c1d6d90e0e0b9db3e
                class: File
                location: whale.xtx
                size: 21
            tags:
            - required
            - command_line_tool
            tool: tests/nameroot.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nameroot/nameext expression in arguments, stdout""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_input_dir_inputbinding(self):
        """Test directory input with inputBinding

        Generated from::

            id: 93
            job: tests/dir-job.yml
            label: input_dir_inputbinding
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: tests/dir6.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory input with inputBinding""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_cl_gen_arrayofarrays(self):
        """Test command line generation of array-of-arrays

        Generated from::

            id: 94
            job: tests/nested-array-job.yml
            label: cl_gen_arrayofarrays
            output:
              echo:
                checksum: sha1$3f786850e387550fdab836ed7e6dc881de23001b
                class: File
                location: echo.txt
                size: 2
            tags:
            - required
            - command_line_tool
            tool: tests/nested-array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line generation of array-of-arrays""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_env_home_tmpdir(self):
        """Test $HOME and $TMPDIR are set correctly

        Generated from::

            id: 95
            job: tests/empty.json
            label: env_home_tmpdir
            output: {}
            tags:
            - shell_command
            - command_line_tool
            tool: tests/envvar.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test $HOME and $TMPDIR are set correctly""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_env_home_tmpdir_docker(self):
        """Test $HOME and $TMPDIR are set correctly in Docker

        Generated from::

            id: 96
            job: tests/empty.json
            label: env_home_tmpdir_docker
            output: {}
            tags:
            - shell_command
            - command_line_tool
            tool: tests/envvar2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test $HOME and $TMPDIR are set correctly in Docker""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_expressionlib_tool_wf_override(self):
        """Test that expressionLib requirement of individual tool step overrides expressionLib of workflow.

        Generated from::

            id: 97
            job: tests/empty.json
            label: expressionlib_tool_wf_override
            output:
              out:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: whatever.txt
                size: 2
            tags:
            - inline_javascript
            - workflow
            tool: tests/js-expr-req-wf.cwl#wf
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that expressionLib requirement of individual tool step overrides expressionLib of workflow.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_output(self):
        """Test output of InitialWorkDir

        Generated from::

            id: 98
            job: tests/initialworkdirrequirement-docker-out-job.json
            label: initial_workdir_output
            output:
              OUTPUT:
                checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                class: File
                location: ref.fasta
                secondaryFiles:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: ref.fasta.fai
                  size: 0
                size: 12010
            tags:
            - docker
            - initial_work_dir
            - command_line_tool
            tool: tests/initialworkdirrequirement-docker-out.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output of InitialWorkDir""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.subworkflow
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_embedded_subworkflow(self):
        """Test embedded subworkflow

        Generated from::

            id: 99
            job: tests/wc-job.json
            label: embedded_subworkflow
            output:
              count_output: 16
            tags:
            - subworkflow
            - workflow
            tool: tests/count-lines10-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test embedded subworkflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.inline_javascript
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_filesarray_secondaryfiles(self):
        """Test required, optional and null secondaryFiles on array of files.

        Generated from::

            id: 100
            job: tests/docker-array-secondaryfiles-job.json
            label: filesarray_secondaryfiles
            output:
              bai_list:
                checksum: sha1$081fc0e57d6efa5f75eeb237aab1d04031132be6
                class: File
                location: fai.list
                size: 386
            tags:
            - docker
            - inline_javascript
            - shell_command
            - command_line_tool
            tool: tests/docker-array-secondaryfiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test required, optional and null secondaryFiles on array of files.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.inline_javascript
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_filesarray_secondaryfiles2(self):
        """Test required, optional and null secondaryFiles on array of files.

        Generated from::

            id: 101
            job: tests/docker-array-secondaryfiles-job2.json
            label: filesarray_secondaryfiles2
            should_fail: true
            tags:
            - docker
            - inline_javascript
            - shell_command
            - command_line_tool
            tool: tests/docker-array-secondaryfiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test required, optional and null secondaryFiles on array of files.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_exprtool_directory_literal(self):
        """Test directory literal output created by ExpressionTool

        Generated from::

            id: 102
            job: tests/dir7.yml
            label: exprtool_directory_literal
            output:
              dir:
                class: Directory
                listing:
                - checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: whale.txt
                  size: 1111
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
                location: a_directory
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/dir7.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory literal output created by ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_exprtool_file_literal(self):
        """Test file literal output created by ExpressionTool

        Generated from::

            id: 103
            job: tests/empty.json
            label: exprtool_file_literal
            output:
              lit:
                checksum: sha1$fea23663b9c8ed71968f86415b5ec091bb111448
                class: File
                location: a_file
                size: 19
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/file-literal-ex.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal output created by ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.docker
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_dockeroutputdir(self):
        """Test dockerOutputDirectory

        Generated from::

            id: 104
            job: tests/empty.json
            label: dockeroutputdir
            output:
              thing:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: thing
                size: 0
            tags:
            - docker
            - command_line_tool
            tool: tests/docker-output-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test dockerOutputDirectory""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_hints_import(self):
        """Test hints with $import

        Generated from::

            id: 105
            job: tests/empty.json
            label: hints_import
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - required
            - command_line_tool
            tool: tests/imported-hint.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test hints with $import""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_default_path_notfound_warning(self):
        """Test warning instead of error when default path is not found

        Generated from::

            id: 106
            job: tests/default_path_job.yml
            label: default_path_notfound_warning
            output: {}
            tags:
            - required
            - command_line_tool
            tool: tests/default_path.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test warning instead of error when default path is not found""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_inlinejs_req_expressions(self):
        """Test InlineJavascriptRequirement with multiple expressions in the same tool

        Generated from::

            id: 107
            job: tests/empty.json
            label: inlinejs_req_expressions
            output:
              args:
              - -A
              - '2'
              - -B
              - baz
              - -C
              - '10'
              - '9'
              - '8'
              - '7'
              - '6'
              - '5'
              - '4'
              - '3'
              - '2'
              - '1'
              - -D
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/inline-js.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InlineJavascriptRequirement with multiple expressions in the same tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_input_dir_recurs_copy_writable(self):
        """Test if a writable input directory is recursively copied and writable

        Generated from::

            id: 108
            job: tests/recursive-input-directory.yml
            label: input_dir_recurs_copy_writable
            output:
              output_dir:
                basename: work_dir
                class: Directory
                listing:
                - basename: a
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/a
                  size: 0
                - basename: b
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/b
                  size: 0
                - basename: c
                  class: Directory
                  listing:
                  - basename: d
                    checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: work_dir/c/d
                    size: 0
                  location: work_dir/c
                - basename: e
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/e
                  size: 0
                location: work_dir
              test_result:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: output.txt
                size: 0
            tags:
            - initial_work_dir
            - shell_command
            - command_line_tool
            tool: tests/recursive-input-directory.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test if a writable input directory is recursively copied and writable""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_null_missing_params(self):
        """Test that missing parameters are null (not undefined) in expression

        Generated from::

            id: 109
            job: tests/empty.json
            label: null_missing_params
            output:
              out: 't
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/null-defined.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that missing parameters are null (not undefined) in expression""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_param_notnull_expr(self):
        """Test that provided parameter is not null in expression

        Generated from::

            id: 110
            job: tests/cat-job.json
            label: param_notnull_expr
            output:
              out: 'f
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/null-defined.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that provided parameter is not null in expression""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_compound_doc(self):
        """Test compound workflow document

        Generated from::

            id: 111
            job: tests/revsort-job.json
            label: wf_compound_doc
            output:
              output:
                checksum: sha1$b9214658cc453331b62c2282b772a5c063dbd284
                class: File
                location: output.txt
                size: 1111
            tags:
            - required
            - workflow
            tool: tests/revsort-packed.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test compound workflow document""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.step_input_expression
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_nameroot_nameext_generated(self):
        """Test that nameroot and nameext are generated from basename at execution time by the runner

        Generated from::

            id: 112
            job: tests/basename-fields-job.yml
            label: nameroot_nameext_generated
            output:
              extFile:
                checksum: sha1$301a72c82a835e1737caf30f94d0eec210c4d9f1
                class: File
                location: Any
                path: Any
                size: 5
              rootFile:
                checksum: sha1$b4a583c391e234cf210e1d576f68f674c8ad7ecd
                class: File
                location: Any
                path: Any
                size: 10
            tags:
            - step_input_expression
            - workflow
            tool: tests/basename-fields-test.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that nameroot and nameext are generated from basename at execution time by the runner""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initialworkpath_output(self):
        """Test that file path in $(inputs) for initialworkdir is in $(outdir).

        Generated from::

            id: 113
            job: tests/wc-job.json
            label: initialworkpath_output
            output: {}
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/initialwork-path.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that file path in $(inputs) for initialworkdir is in $(outdir).""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.multiple_input
    @pytest.mark.inline_javascript
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_twopar_oneinput_flattenedmerge(self):
        """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior. Workflow inputs are set as list

        Generated from::

            id: 114
            job: tests/count-lines6-job.json
            label: wf_scatter_twopar_oneinput_flattenedmerge
            output:
              count_output: 34
            tags:
            - multiple_input
            - inline_javascript
            - workflow
            tool: tests/count-lines12-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior. Workflow inputs are set as list""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.multiple_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_multiplesources_multipletypes(self):
        """Test step input with multiple sources with multiple types

        Generated from::

            id: 115
            job: tests/sum-job.json
            label: wf_multiplesources_multipletypes
            output:
              result: 12
            tags:
            - step_input
            - inline_javascript
            - multiple_input
            - workflow
            tool: tests/sum-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test step input with multiple sources with multiple types""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_shelldir_notinterpreted(self):
        """Test that shell directives are not interpreted.

        Generated from::

            id: 116
            job: tests/empty.json
            label: shelldir_notinterpreted
            output:
              stderr_file:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              stdout_file:
                checksum: sha1$1555252d52d4ec3262538a4426a83a99cfff4402
                class: File
                location: Any
                size: 9
            tags:
            - required
            - command_line_tool
            tool: tests/shellchar.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that shell directives are not interpreted.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_shelldir_quoted(self):
        """Test that shell directives are quoted.

        Generated from::

            id: 117
            job: tests/empty.json
            label: shelldir_quoted
            output:
              stderr_file:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              stdout_file:
                checksum: sha1$1555252d52d4ec3262538a4426a83a99cfff4402
                class: File
                location: Any
                size: 9
            tags:
            - shell_command
            - command_line_tool
            tool: tests/shellchar2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that shell directives are quoted.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_empty_writable(self):
        """Test empty writable dir with InitialWorkDirRequirement

        Generated from::

            id: 118
            job: tests/empty.json
            label: initial_workdir_empty_writable
            output:
              out:
                basename: emptyWritableDir
                class: Directory
                listing:
                - basename: blurg
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: blurg
                  size: 0
                location: emptyWritableDir
            tags:
            - inline_javascript
            - initial_work_dir
            - command_line_tool
            tool: tests/writable-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test empty writable dir with InitialWorkDirRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inline_javascript
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_workdir_empty_writable_docker(self):
        """Test empty writable dir with InitialWorkDirRequirement inside Docker

        Generated from::

            id: 119
            job: tests/empty.json
            label: initial_workdir_empty_writable_docker
            output:
              out:
                basename: emptyWritableDir
                class: Directory
                listing:
                - basename: blurg
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: blurg
                  size: 0
                location: emptyWritableDir
            tags:
            - inline_javascript
            - initial_work_dir
            - command_line_tool
            tool: tests/writable-dir-docker.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test empty writable dir with InitialWorkDirRequirement inside Docker""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_inputs(self):
        """Test dynamic resource reqs referencing inputs

        Generated from::

            id: 120
            job: tests/dynresreq-job.yaml
            label: dynamic_resreq_inputs
            output:
              output:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - command_line_tool
            tool: tests/dynresreq.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test dynamic resource reqs referencing inputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_fileliteral_input_docker(self):
        """Test file literal as input without Docker

        Generated from::

            id: 121
            job: tests/file-literal.yml
            label: fileliteral_input_docker
            output:
              output_file:
                checksum: sha1$d0e04ff6c413c7d57f9a0ca0a33cd3ab52e2dd9c
                class: File
                location: output.txt
                size: 18
            tags:
            - required
            - command_line_tool
            tool: tests/cat3-nodocker.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal as input without Docker""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_outputbinding_glob_sorted(self):
        """Test that OutputBinding.glob is sorted as specified by POSIX

        Generated from::

            id: 122
            job: tests/empty.json
            label: outputbinding_glob_sorted
            output:
              letters:
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: a
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: b
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: c
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: w
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: x
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: y
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: z
                size: 0
            tags:
            - required
            - command_line_tool
            tool: tests/glob_test.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that OutputBinding.glob is sorted as specified by POSIX""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_initialworkdir_nesteddir(self):
        """Test InitialWorkDirRequirement with a nested directory structure from another step

        Generated from::

            id: 123
            job: tests/empty.json
            label: initialworkdir_nesteddir
            output:
              ya_empty:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: ya
                size: 0
            tags:
            - initial_work_dir
            - workflow
            tool: tests/iwdr_with_nested_dirs.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement with a nested directory structure from another step""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_booleanflags_cl_noinputbinding(self):
        """Test that boolean flags do not appear on command line if inputBinding is empty and not null

        Generated from::

            id: 124
            job: tests/bool-empty-inputbinding-job.json
            label: booleanflags_cl_noinputbinding
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/bool-empty-inputbinding.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that boolean flags do not appear on command line if inputBinding is empty and not null""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_expr_reference_self_noinput(self):
        """Test that expression engine does not fail to evaluate reference to self with unprovided input

        Generated from::

            id: 125
            job: tests/empty.json
            label: expr_reference_self_noinput
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/stage-unprovided-file.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that expression engine does not fail to evaluate reference to self with unprovided input""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_success_codes(self):
        """Test successCodes

        Generated from::

            id: 126
            job: tests/empty.json
            label: success_codes
            output: {}
            tags:
            - required
            - command_line_tool
            tool: tests/exit-success.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test successCodes""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_wf(self):
        """Test simple workflow with a dynamic resource requirement

        Generated from::

            id: 127
            job: tests/dynresreq-job.yaml
            label: dynamic_resreq_wf
            output:
              cores:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: output
                size: 2
            tags:
            - resource
            - workflow
            tool: tests/dynresreq-workflow.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple workflow with a dynamic resource requirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_cl_empty_array_input(self):
        """Test that empty array input does not add anything to command line

        Generated from::

            id: 128
            job: tests/empty-array-job.json
            label: cl_empty_array_input
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/empty-array-input.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that empty array input does not add anything to command line""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_resreq_step_overrides_wf(self):
        """Test that ResourceRequirement on a step level redefines requirement on the workflow level

        Generated from::

            id: 129
            job: tests/empty.json
            label: resreq_step_overrides_wf
            output:
              out:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - workflow
            tool: tests/steplevel-resreq.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that ResourceRequirement on a step level redefines requirement on the workflow level""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_valuefrom_constant_overrides_inputs(self):
        """Test valueFrom with constant value overriding provided array inputs

        Generated from::

            id: 130
            job: tests/array-of-strings-job.yml
            label: valuefrom_constant_overrides_inputs
            output:
              args:
              - replacementValue
            tags:
            - required
            - command_line_tool
            tool: tests/valueFrom-constant.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom with constant value overriding provided array inputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_filesizes(self):
        """Test dynamic resource reqs referencing the size of Files inside a Directory

        Generated from::

            id: 131
            job: tests/dynresreq-dir-job.yaml
            label: dynamic_resreq_filesizes
            output:
              output:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - command_line_tool
            tool: tests/dynresreq-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test dynamic resource reqs referencing the size of Files inside a Directory""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_step_connect_undeclared_param(self):
        """Test that it is not an error to connect a parameter to a workflow step, even if the parameter doesn't appear in the `run` process inputs.

        Generated from::

            id: 132
            job: tests/empty.json
            label: wf_step_connect_undeclared_param
            output:
              out: 'hello inp1
            
                '
            tags:
            - required
            - workflow
            tool: tests/pass-unconnected.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that it is not an error to connect a parameter to a workflow step, even if the parameter doesn't appear in the `run` process inputs.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.workflow
    @pytest.mark.green
    def test_conformance_v1_1_wf_step_access_undeclared_param(self):
        """Test that parameters that don't appear in the `run` process inputs are not present in the input object used to run the tool.

        Generated from::

            id: 133
            job: tests/empty.json
            label: wf_step_access_undeclared_param
            should_fail: true
            tags:
            - required
            - workflow
            tool: tests/fail-unconnected.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that parameters that don't appear in the `run` process inputs are not present in the input object used to run the tool.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_env_home_tmpdir_docker_no_return_code(self):
        """Test $HOME and $TMPDIR are set correctly in Docker without using return code

        Generated from::

            id: 134
            job: tests/empty.json
            label: env_home_tmpdir_docker_no_return_code
            output:
              results:
                basename: results
                checksum: sha1$7d5ca8c0c03e883c56c4eb1ef6f6bb9bccad4d86
                class: File
                size: 8
            tags:
            - shell_command
            - command_line_tool
            tool: tests/envvar3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test $HOME and $TMPDIR are set correctly in Docker without using return code""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.scatter
    @pytest.mark.step_input
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_wf_scatter_oneparam_valuefrom_inputs(self):
        """Test workflow scatter with single scatter parameter and two valueFrom using $inputs (first and current el)

        Generated from::

            id: 135
            job: tests/scatter-valuefrom-job1.json
            label: wf_scatter_oneparam_valuefrom_inputs
            output:
              out:
              - foo one one
              - foo one two
              - foo one three
              - foo one four
            tags:
            - scatter
            - step_input
            - workflow
            tool: tests/scatter-valuefrom-inputs-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow scatter with single scatter parameter and two valueFrom using $inputs (first and current el)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.schema_def
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_packed_import_schema(self):
        """SchemaDefRequirement with $import, and packed

        Generated from::

            id: 136
            job: tests/import_schema-def_job.yml
            label: packed_import_schema
            output:
              output_bam:
                basename: a.bam
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                size: 0
            tags:
            - schema_def
            - workflow
            tool: tests/import_schema-def_packed.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """SchemaDefRequirement with $import, and packed""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_job_input_secondary_subdirs(self):
        """Test specifying secondaryFiles in subdirectories of the job input document.

        Generated from::

            id: 137
            job: tests/dir4-subdir-1-job.yml
            label: job_input_secondary_subdirs
            output:
              outlist:
                checksum: sha1$9d9bc8f5252d39274b5dfbac64216c6e888f5dfc
                class: File
                location: output.txt
                size: 14
            tags:
            - shell_command
            - command_line_tool
            tool: tests/dir4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test specifying secondaryFiles in subdirectories of the job input document.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.shell_command
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_job_input_subdir_primary_and_secondary_subdirs(self):
        """Test specifying secondaryFiles in same subdirectory of the job input as the primary input file.

        Generated from::

            id: 138
            job: tests/dir4-subdir-2-job.yml
            label: job_input_subdir_primary_and_secondary_subdirs
            output:
              outlist:
                checksum: sha1$9d9bc8f5252d39274b5dfbac64216c6e888f5dfc
                class: File
                location: output.txt
                size: 14
            tags:
            - shell_command
            - command_line_tool
            tool: tests/dir4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test specifying secondaryFiles in same subdirectory of the job input as the primary input file.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_scatter_embedded_subworkflow(self):
        """Test simple scatter over an embedded subworkflow

        Generated from::

            id: 139
            job: tests/count-lines3-job.json
            label: scatter_embedded_subworkflow
            output:
              count_output:
              - 16
              - 1
            tags:
            - workflow
            - inline_javascript
            tool: tests/count-lines18-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple scatter over an embedded subworkflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.scatter
    @pytest.mark.subworkflow
    @pytest.mark.multiple_input
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_scatter_multi_input_embedded_subworkflow(self):
        """Test simple multiple input scatter over an embedded subworkflow

        Generated from::

            id: 140
            job: tests/count-lines4-job.json
            label: scatter_multi_input_embedded_subworkflow
            output:
              count_output:
              - 16
              - 1
            tags:
            - workflow
            - scatter
            - subworkflow
            - multiple_input
            - inline_javascript
            tool: tests/count-lines14-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple multiple input scatter over an embedded subworkflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.subworkflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_embedded_subworkflow_embedded_subsubworkflow(self):
        """Test twice nested subworkflow

        Generated from::

            id: 141
            job: tests/wc-job.json
            label: workflow_embedded_subworkflow_embedded_subsubworkflow
            output:
              count_output: 16
            tags:
            - workflow
            - subworkflow
            - inline_javascript
            tool: tests/count-lines15-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test twice nested subworkflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.subworkflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_embedded_subworkflow_with_tool_and_subsubworkflow(self):
        """Test subworkflow of mixed depth with tool first

        Generated from::

            id: 142
            job: tests/wc-job.json
            label: workflow_embedded_subworkflow_with_tool_and_subsubworkflow
            output:
              count_output: 16
            tags:
            - workflow
            - subworkflow
            - inline_javascript
            tool: tests/count-lines16-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test subworkflow of mixed depth with tool first""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.subworkflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_embedded_subworkflow_with_subsubworkflow_and_tool(self):
        """Test subworkflow of mixed depth with tool after

        Generated from::

            id: 143
            job: tests/wc-job.json
            label: workflow_embedded_subworkflow_with_subsubworkflow_and_tool
            output:
              count_output: 16
            tags:
            - workflow
            - subworkflow
            - inline_javascript
            tool: tests/count-lines17-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test subworkflow of mixed depth with tool after""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.shell_command
    @pytest.mark.red
    def test_conformance_v1_1_workflow_records_inputs_and_outputs(self):
        """Test record type inputs to and outputs from workflows.

        Generated from::

            id: 144
            job: tests/record-output-job.json
            label: workflow_records_inputs_and_outputs
            output:
              orec:
                obar:
                  checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                  class: File
                  location: bar
                  size: 12010
                ofoo:
                  checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: foo
                  size: 1111
            tags:
            - workflow
            - shell_command
            tool: tests/record-output-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test record type inputs to and outputs from workflows.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input(self):
        """Test integer workflow input and outputs

        Generated from::

            id: 145
            job: tests/io-int.json
            label: workflow_integer_input
            output:
              o: 10
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test integer workflow input and outputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input_optional_specified(self):
        """Test optional integer workflow inputs (specified)

        Generated from::

            id: 146
            job: tests/io-int.json
            label: workflow_integer_input_optional_specified
            output:
              o: 10
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-optional-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test optional integer workflow inputs (specified)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input_optional_unspecified(self):
        """Test optional integer workflow inputs (unspecified)

        Generated from::

            id: 147
            job: tests/empty.json
            label: workflow_integer_input_optional_unspecified
            output:
              o: 4
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-optional-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test optional integer workflow inputs (unspecified)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input_default_specified(self):
        """Test default integer workflow inputs (specified)

        Generated from::

            id: 148
            job: tests/io-int.json
            label: workflow_integer_input_default_specified
            output:
              o: 10
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default integer workflow inputs (specified)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input_default_unspecified(self):
        """Test default integer workflow inputs (unspecified)

        Generated from::

            id: 149
            job: tests/empty.json
            label: workflow_integer_input_default_unspecified
            output:
              o: 8
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default integer workflow inputs (unspecified)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_integer_input_default_and_tool_integer_input_default(self):
        """Test default integer tool and workflow inputs (unspecified)

        Generated from::

            id: 150
            job: tests/empty.json
            label: workflow_integer_input_default_and_tool_integer_input_default
            output:
              o: 13
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-int-default-tool-and-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default integer tool and workflow inputs (unspecified)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_workflow_file_input_default_unspecified(self):
        """Test File input with default unspecified to workflow

        Generated from::

            id: 151
            job: tests/empty.json
            label: workflow_file_input_default_unspecified
            output:
              o:
                basename: output
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: Any
                size: 1111
            tags:
            - workflow
            tool: tests/io-file-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test File input with default unspecified to workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_workflow_file_input_default_specified(self):
        """Test File input with default specified to workflow

        Generated from::

            id: 152
            job: tests/default_path_job.yml
            label: workflow_file_input_default_specified
            output:
              o:
                basename: output
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: Any
                size: 13
            tags:
            - workflow
            tool: tests/io-file-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test File input with default specified to workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_clt_optional_union_input_file_or_files_with_array_of_one_file_provided(self):
        """Test input union type or File or File array to a tool with one file in array specified.

        Generated from::

            id: 153
            job: tests/job-input-array-one-empty-file.json
            label: clt_optional_union_input_file_or_files_with_array_of_one_file_provided
            output:
              output_file:
                basename: output.txt
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-file-or-files.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test input union type or File or File array to a tool with one file in array specified.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_clt_optional_union_input_file_or_files_with_many_files_provided(self):
        """Test input union type or File or File array to a tool with a few files in array specified.

        Generated from::

            id: 154
            job: tests/job-input-array-few-files.json
            label: clt_optional_union_input_file_or_files_with_many_files_provided
            output:
              output_file:
                basename: output.txt
                checksum: sha1$6d1723861ad5a1260f1c3c07c93076c5a215f646
                class: File
                location: Any
                size: 1114
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-file-or-files.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test input union type or File or File array to a tool with a few files in array specified.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_optional_union_input_file_or_files_with_single_file_provided(self):
        """Test input union type or File or File array to a tool with one file specified.

        Generated from::

            id: 155
            job: tests/job-input-one-file.json
            label: clt_optional_union_input_file_or_files_with_single_file_provided
            output:
              output_file:
                basename: output.txt
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: Any
                size: 1111
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-file-or-files.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test input union type or File or File array to a tool with one file specified.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_optional_union_input_file_or_files_with_nothing_provided(self):
        """Test input union type or File or File array to a tool with null specified.

        Generated from::

            id: 156
            job: tests/job-input-null.json
            label: clt_optional_union_input_file_or_files_with_nothing_provided
            output:
              output_file:
                basename: output.txt
                checksum: sha1$503458abf7614be3fb26d85ff5d8f3e17aa0a552
                class: File
                location: Any
                size: 10
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-file-or-files.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test input union type or File or File array to a tool with null specified.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_any_input_with_integer_provided(self):
        """Test Any parameter with integer input to a tool

        Generated from::

            id: 157
            job: tests/io-any-int.json
            label: clt_any_input_with_integer_provided
            output:
              t1: 7
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-any-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with integer input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_any_input_with_string_provided(self):
        """Test Any parameter with string input to a tool

        Generated from::

            id: 158
            job: tests/io-any-string.json
            label: clt_any_input_with_string_provided
            output:
              t1: '7'
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-any-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with string input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_any_input_with_file_provided(self):
        """Test Any parameter with file input to a tool

        Generated from::

            id: 159
            job: tests/io-any-file.json
            label: clt_any_input_with_file_provided
            output:
              t1: File
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-any-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with file input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_clt_any_input_with_mixed_array_provided(self):
        """Test Any parameter with array input to a tool

        Generated from::

            id: 160
            job: tests/io-any-array.json
            label: clt_any_input_with_mixed_array_provided
            output:
              t1:
              - 1
              - moocow
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-any-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with array input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_clt_any_input_with_record_provided(self):
        """Test Any parameter with record input to a tool

        Generated from::

            id: 161
            job: tests/io-any-record.json
            label: clt_any_input_with_record_provided
            output:
              t1:
                cow: 5
                moo: 1
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/io-any-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with record input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_any_input_with_integer_provided(self):
        """Test Any parameter with integer input to a workflow

        Generated from::

            id: 162
            job: tests/io-any-int.json
            label: workflow_any_input_with_integer_provided
            output:
              t1: 7
            tags:
            - workflow
            - inline_javascript
            tool: tests/io-any-wf-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with integer input to a workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_any_input_with_string_provided(self):
        """Test Any parameter with string input to a workflow

        Generated from::

            id: 163
            job: tests/io-any-string.json
            label: workflow_any_input_with_string_provided
            output:
              t1: '7'
            tags:
            - workflow
            - inline_javascript
            tool: tests/io-any-wf-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with string input to a workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_any_input_with_file_provided(self):
        """Test Any parameter with file input to a workflow

        Generated from::

            id: 164
            job: tests/io-any-file.json
            label: workflow_any_input_with_file_provided
            output:
              t1: File
            tags:
            - workflow
            - inline_javascript
            tool: tests/io-any-wf-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with file input to a workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_any_input_with_mixed_array_provided(self):
        """Test Any parameter with array input to a workflow

        Generated from::

            id: 165
            job: tests/io-any-array.json
            label: workflow_any_input_with_mixed_array_provided
            output:
              t1:
              - 1
              - moocow
            tags:
            - workflow
            - inline_javascript
            tool: tests/io-any-wf-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with array input to a workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_any_input_with_record_provided(self):
        """Test Any parameter with record input to a tool

        Generated from::

            id: 166
            job: tests/io-any-record.json
            label: workflow_any_input_with_record_provided
            output:
              t1:
                cow: 5
                moo: 1
            tags:
            - workflow
            - inline_javascript
            tool: tests/io-any-wf-1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any parameter with record input to a tool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_workflow_union_default_input_unspecified(self):
        """Test union type input to workflow with default unspecified

        Generated from::

            id: 167
            job: tests/empty.json
            label: workflow_union_default_input_unspecified
            output:
              o: the default value
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-union-input-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test union type input to workflow with default unspecified""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.green
    def test_conformance_v1_1_workflow_union_default_input_with_file_provided(self):
        """Test union type input to workflow with default specified as file

        Generated from::

            id: 168
            job: tests/io-any-file.json
            label: workflow_union_default_input_with_file_provided
            output:
              o: File
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-union-input-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test union type input to workflow with default specified as file""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.red
    def test_conformance_v1_1_workflowstep_valuefrom_string(self):
        """Test valueFrom on workflow step from literal (string).

        Generated from::

            id: 169
            job: tests/empty.json
            label: workflowstep_valuefrom_string
            output:
              val: 'moocow
            
                '
            tags:
            - workflow
            - step_input
            tool: tests/step-valuefrom4-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom on workflow step from literal (string).""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.red
    def test_conformance_v1_1_workflowstep_valuefrom_file_basename(self):
        """Test valueFrom on workflow step using basename.

        Generated from::

            id: 170
            job: tests/wc-job.json
            label: workflowstep_valuefrom_file_basename
            output:
              val1: 'whale.txt
            
                '
              val2: 'step1_out
            
                '
            tags:
            - workflow
            - step_input
            tool: tests/step-valuefrom5-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom on workflow step using basename.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.expression_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_expression_tool_int_array_output(self):
        """Test output arrays in a tool (with ints).

        Generated from::

            id: 171
            job: tests/output-arrays-int-job.json
            label: expression_tool_int_array_output
            output:
              o:
              - 0
              - 1
              - 2
            tags:
            - expression_tool
            - inline_javascript
            tool: tests/output-arrays-int.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output arrays in a tool (with ints).""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.expression_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflowstep_int_array_input_output(self):
        """Test output arrays in a workflow (with ints).

        Generated from::

            id: 172
            job: tests/output-arrays-int-job.json
            label: workflowstep_int_array_input_output
            output:
              o: 12
            tags:
            - workflow
            - expression_tool
            - inline_javascript
            tool: tests/output-arrays-int-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output arrays in a workflow (with ints).""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.expression_tool
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_workflow_file_array_output(self):
        """Test output arrays in a workflow (with Files).

        Generated from::

            id: 173
            job: tests/output-arrays-file-job.json
            label: workflow_file_array_output
            output:
              o:
              - basename: moo
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              - basename: cow
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
            tags:
            - workflow
            - expression_tool
            - inline_javascript
            tool: tests/output-arrays-file-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output arrays in a workflow (with Files).""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.docker
    @pytest.mark.red
    def test_conformance_v1_1_docker_entrypoint(self):
        """Test Docker ENTRYPOINT usage

        Generated from::

            id: 174
            job: tests/empty.json
            label: docker_entrypoint
            output:
              cow:
                basename: cow
                checksum: sha1$7a788f56fa49ae0ba5ebde780efe4d6a89b5db47
                class: File
                location: Any
                size: 4
            tags:
            - command_line_tool
            - docker
            tool: tests/docker-run-cmd.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Docker ENTRYPOINT usage""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_file_size_property_with_empty_file(self):
        """Test use of size in expressions for an empty file

        Generated from::

            id: 175
            job: tests/job-input-array-one-empty-file.json
            label: clt_file_size_property_with_empty_file
            output:
              output_file:
                basename: output.txt
                checksum: sha1$dad5a8472b87f6c5ef87d8fc6ef1458defc57250
                class: File
                location: Any
                size: 11
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/size-expression-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of size in expressions for an empty file""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_clt_file_size_property_with_multi_file(self):
        """Test use of size in expressions for a few files

        Generated from::

            id: 176
            job: tests/job-input-array-few-files.json
            label: clt_file_size_property_with_multi_file
            output:
              output_file:
                basename: output.txt
                checksum: sha1$9def39730e8012bd09bf8387648982728501737d
                class: File
                location: Any
                size: 31
            tags:
            - command_line_tool
            - inline_javascript
            tool: tests/size-expression-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of size in expressions for a few files""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_any_without_defaults_unspecified_fails(self):
        """Test Any without defaults, unspecified, should fail.

        Generated from::

            id: 177
            job: tests/null-expression-echo-job.json
            label: any_without_defaults_unspecified_fails
            should_fail: true
            tags:
            - command_line_tool
            - required
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults, unspecified, should fail.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_any_without_defaults_specified_fails(self):
        """Test Any without defaults, specified, should fail.

        Generated from::

            id: 178
            job: tests/null-expression1-job.json
            label: any_without_defaults_specified_fails
            should_fail: true
            tags:
            - command_line_tool
            - required
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults, specified, should fail.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_noexp(self):
        """Test default value on step input parameter, no ExpressionTool

        Generated from::

            id: 179
            job: tests/empty.json
            label: step_input_default_value_noexp
            output:
              wc_output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                size: 3
            tags:
            - workflow
            - required
            tool: tests/count-lines9-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter, no ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden_noexp(self):
        """Test default value on step input parameter overridden by provided source, no ExpressionTool

        Generated from::

            id: 180
            job: tests/cat-job.json
            label: step_input_default_value_overriden_noexp
            output:
              wc_output:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                size: 2
            tags:
            - workflow
            - required
            tool: tests/count-lines11-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source, no ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.subworkflow
    @pytest.mark.red
    def test_conformance_v1_1_nested_workflow_noexp(self):
        """Test nested workflow, without ExpressionTool

        Generated from::

            id: 181
            job: tests/wc-job.json
            label: nested_workflow_noexp
            output:
              wc_output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                size: 3
            tags:
            - workflow
            - subworkflow
            tool: tests/count-lines8-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested workflow, without ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.multiple_input
    @pytest.mark.red
    def test_conformance_v1_1_wf_multiplesources_multipletypes_noexp(self):
        """Test step input with multiple sources with multiple types, without ExpressionTool

        Generated from::

            id: 182
            job: tests/sum-job.json
            label: wf_multiplesources_multipletypes_noexp
            output:
              result:
                checksum: sha1$ad552e6dc057d1d825bf49df79d6b98eba846ebe
                class: File
                size: 3
            tags:
            - workflow
            - step_input
            - inline_javascript
            - multiple_input
            tool: tests/sum-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test step input with multiple sources with multiple types, without ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.resource
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_wf_optional_file_default(self):
        """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The CommandLineTool input has a default value (a local file) and the workflow nor the workflow step does not provide any value for this input.

        Generated from::

            id: 183
            job: tests/empty.json
            label: dynamic_resreq_wf_optional_file_default
            output:
              cores:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: output
                size: 2
            tags:
            - workflow
            - resource
            tool: tests/dynresreq-workflow-tooldefault.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The CommandLineTool input has a default value (a local file) and the workflow nor the workflow step does not provide any value for this input.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.resource
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_wf_optional_file_step_default(self):
        """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The workflow step provides a default value (a local file) for this input and the workflow itself does not provide any value for this input.

        Generated from::

            id: 184
            job: tests/empty.json
            label: dynamic_resreq_wf_optional_file_step_default
            output:
              cores:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: output
                size: 2
            tags:
            - workflow
            - resource
            tool: tests/dynresreq-workflow-stepdefault.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The workflow step provides a default value (a local file) for this input and the workflow itself does not provide any value for this input.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.resource
    @pytest.mark.red
    def test_conformance_v1_1_dynamic_resreq_wf_optional_file_wf_default(self):
        """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The workflow itelf provides a default value (a local file) for this input.

        Generated from::

            id: 185
            job: tests/empty.json
            label: dynamic_resreq_wf_optional_file_wf_default
            output:
              cores:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: output
                size: 2
            tags:
            - workflow
            - resource
            tool: tests/dynresreq-workflow-inputdefault.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Within a workflow, test accessing the size attribute of an optional input File as part of a CommandLineTool's ResourceRequirement calculation. The workflow itelf provides a default value (a local file) for this input.""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step(self):
        """Test default value on step input parameter overridden by provided source. With passthrough first step

        Generated from::

            id: 186
            job: tests/cat-job.json
            label: step_input_default_value_overriden_2nd_step
            output:
              count_output: 1
            tags:
            - workflow
            - inline_javascript
            tool: tests/count-lines11-extra-step-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With passthrough first step""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step_noexp(self):
        """Test default value on step input parameter overridden by provided source. With passthrough first step and no ExpressionTool

        Generated from::

            id: 187
            job: tests/cat-job.json
            label: step_input_default_value_overriden_2nd_step_noexp
            output:
              wc_output:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                size: 2
            tags:
            - workflow
            - required
            tool: tests/count-lines11-extra-step-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With passthrough first step and no ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step_null(self):
        """Test default value on step input parameter overridden by provided source. With null producing first step

        Generated from::

            id: 188
            job: tests/empty.json
            label: step_input_default_value_overriden_2nd_step_null
            output:
              count_output: 16
            tags:
            - workflow
            - inline_javascript
            tool: tests/count-lines11-null-step-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With null producing first step""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step_null_noexp(self):
        """Test default value on step input parameter overridden by provided source. With null producing first step and no ExpressionTool

        Generated from::

            id: 189
            job: tests/empty.json
            label: step_input_default_value_overriden_2nd_step_null_noexp
            output:
              wc_output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                size: 3
            tags:
            - workflow
            - required
            tool: tests/count-lines11-null-step-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With null producing first step and no ExpressionTool""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_stdin_from_directory_literal_with_local_file(self):
        """Pipe to stdin from user provided local File via a Directory literal

        Generated from::

            id: 190
            job: tests/cat-from-dir-job.yaml
            label: stdin_from_directory_literal_with_local_file
            output:
              output:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                size: 13
            tags:
            - command_line_tool
            - required
            tool: tests/cat-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Pipe to stdin from user provided local File via a Directory literal""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_stdin_from_directory_literal_with_literal_file(self):
        """Pipe to stdin from literal File via a Directory literal

        Generated from::

            id: 191
            job: tests/cat-from-dir-with-literal-file.yaml
            label: stdin_from_directory_literal_with_literal_file
            output:
              output:
                checksum: sha1$ef88e689559565999700d6fea7cf7ba306d04360
                class: File
                size: 26
            tags:
            - command_line_tool
            - required
            tool: tests/cat-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Pipe to stdin from literal File via a Directory literal""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_directory_literal_with_literal_file_nostdin(self):
        """Test non-stdin reference to literal File via a Directory literal

        Generated from::

            id: 192
            job: tests/cat-from-dir-with-literal-file.yaml
            label: directory_literal_with_literal_file_nostdin
            output:
              output_file:
                checksum: sha1$ef88e689559565999700d6fea7cf7ba306d04360
                class: File
                size: 26
            tags:
            - command_line_tool
            - required
            tool: tests/cat3-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test non-stdin reference to literal File via a Directory literal""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_no_inputs_commandlinetool(self):
        """Test CommandLineTool without inputs

        Generated from::

            id: 193
            label: no_inputs_commandlinetool
            output:
              output:
                checksum: sha1$1334e67fe9eb70db8ae14ccfa6cfb59e2cc24eae
                class: File
                location: output
                size: 4
            tags:
            - command_line_tool
            - required
            tool: tests/no-inputs-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test CommandLineTool without inputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_no_outputs_commandlinetool(self):
        """Test CommandLineTool without outputs

        Generated from::

            id: 194
            job: tests/cat-job.json
            label: no_outputs_commandlinetool
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/no-outputs-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test CommandLineTool without outputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_no_inputs_workflow(self):
        """Test Workflow without inputs

        Generated from::

            id: 195
            label: no_inputs_workflow
            output:
              output:
                checksum: sha1$1334e67fe9eb70db8ae14ccfa6cfb59e2cc24eae
                class: File
                location: output
                size: 4
            tags:
            - workflow
            - required
            tool: tests/no-inputs-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Workflow without inputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_no_outputs_workflow(self):
        """Test Workflow without outputs

        Generated from::

            id: 196
            job: tests/cat-job.json
            label: no_outputs_workflow
            output: {}
            tags:
            - workflow
            - required
            tool: tests/no-outputs-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Workflow without outputs""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_anonymous_enum_in_array(self):
        """Test an anonymous enum inside an array inside a record

        Generated from::

            id: 197
            job: tests/anon_enum_inside_array.yml
            label: anonymous_enum_in_array
            output:
              result:
                checksum: sha1$2132943d72c39423e0b9425cbc40dfd5bf3e9cb2
                class: File
                size: 39
            tags:
            - command_line_tool
            - required
            tool: tests/anon_enum_inside_array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test an anonymous enum inside an array inside a record""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.schema_def
    @pytest.mark.red
    def test_conformance_v1_1_schema_def_anonymous_enum_in_array(self):
        """Test an anonymous enum inside an array inside a record, SchemaDefRequirement

        Generated from::

            id: 198
            job: tests/anon_enum_inside_array_inside_schemadef.yml
            label: schema-def_anonymous_enum_in_array
            output:
              result:
                checksum: sha1$f17c7d81f66e1520fca25b96b90eeeae5bbf08b0
                class: File
                size: 39
            tags:
            - command_line_tool
            - schema_def
            tool: tests/anon_enum_inside_array_inside_schemadef.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test an anonymous enum inside an array inside a record, SchemaDefRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.docker
    @pytest.mark.red
    def test_conformance_v1_1_stdin_shorcut(self):
        """Test command execution in with stdin and stdout redirection using stdin shortcut

        Generated from::

            id: 199
            job: tests/wc-job.json
            label: stdin_shorcut
            output:
              output:
                checksum: sha1$2936abd60952276ffbf91d709b19c6c48c263947
                class: File
                location: output
                size: 24
            tags:
            - command_line_tool
            - docker
            tool: tests/wc-tool-shortcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in with stdin and stdout redirection using stdin shortcut""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_secondary_files_in_unnamed_records(self):
        """Test secondaryFiles on anonymous record fields

        Generated from::

            id: 200
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_in_unnamed_records
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/record-in-secondaryFiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles on anonymous record fields""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.schema_def
    @pytest.mark.red
    def test_conformance_v1_1_secondary_files_in_named_records(self):
        """Test secondaryFiles on SchemaDefRequirement record fields

        Generated from::

            id: 201
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_in_named_records
            output: {}
            tags:
            - command_line_tool
            - schema_def
            tool: tests/record-sd-secondaryFiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles on SchemaDefRequirement record fields""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_secondary_files_in_output_records(self):
        """Test secondaryFiles on output record fields

        Generated from::

            id: 202
            job: tests/empty.json
            label: secondary_files_in_output_records
            output:
              record_output:
                f1:
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: A
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: A.s2
                    size: 0
                  size: 0
                f2:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: B
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: B.s3
                    size: 0
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: C
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: C.s3
                    size: 0
                  size: 0
            tags:
            - command_line_tool
            - required
            tool: tests/record-out-secondaryFiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles on output record fields""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_secondary_files_workflow_propagation(self):
        """Test secondaryFiles propagation through workflow

        Generated from::

            id: 203
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_workflow_propagation
            output: {}
            tags:
            - workflow
            - required
            tool: tests/record-in-secondaryFiles-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles propagation through workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_secondary_files_missing(self):
        """Test checking when secondaryFiles are missing

        Generated from::

            id: 204
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_missing
            should_fail: true
            tags:
            - workflow
            - required
            tool: tests/record-in-secondaryFiles-missing-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test checking when secondaryFiles are missing""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_input_records_file_entry_with_format(self):
        """Test format on anonymous record fields

        Generated from::

            id: 205
            job: tests/record-format-job.yml
            label: input_records_file_entry_with_format
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/record-in-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format on anonymous record fields""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.format_checking
    @pytest.mark.green
    def test_conformance_v1_1_input_records_file_entry_with_format_and_bad_regular_input_file_format(self):
        """Test file format checking on parameter

        Generated from::

            id: 206
            job: tests/record-format-job2.yml
            label: input_records_file_entry_with_format_and_bad_regular_input_file_format
            should_fail: true
            tags:
            - command_line_tool
            - format_checking
            tool: tests/record-in-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file format checking on parameter""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.format_checking
    @pytest.mark.green
    def test_conformance_v1_1_input_records_file_entry_with_format_and_bad_entry_file_format(self):
        """Test file format checking on record field

        Generated from::

            id: 207
            job: tests/record-format-job3.yml
            label: input_records_file_entry_with_format_and_bad_entry_file_format
            should_fail: true
            tags:
            - command_line_tool
            - format_checking
            tool: tests/record-in-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file format checking on record field""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.format_checking
    @pytest.mark.green
    def test_conformance_v1_1_input_records_file_entry_with_format_and_bad_entry_array_file_format(self):
        """Test file format checking on array item

        Generated from::

            id: 208
            job: tests/record-format-job4.yml
            label: input_records_file_entry_with_format_and_bad_entry_array_file_format
            should_fail: true
            tags:
            - command_line_tool
            - format_checking
            tool: tests/record-in-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file format checking on array item""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.format_checking
    @pytest.mark.red
    def test_conformance_v1_1_record_output_file_entry_format(self):
        """Test format on output record fields

        Generated from::

            id: 209
            job: tests/record-secondaryFiles-job.yml
            label: record_output_file_entry_format
            output:
              f1out:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                format: http://example.com/format1
                location: A
                size: 0
              record_output:
                f2out:
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  format: http://example.com/format2
                  location: B
                  size: 0
            tags:
            - command_line_tool
            - format_checking
            tool: tests/record-out-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format on output record fields""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_input_inputBinding_loadContents(self):
        """Test WorkflowInputParameter.inputBinding.loadContents

        Generated from::

            id: 210
            job: tests/wf-loadContents-job.yml
            label: workflow_input_inputBinding_loadContents
            output:
              my_int: 42
            tags:
            - workflow
            - step_input
            - inline_javascript
            - expression_tool
            tool: tests/wf-loadContents.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test WorkflowInputParameter.inputBinding.loadContents""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_input_loadContents_without_inputBinding(self):
        """Test WorkflowInputParameter.loadContents

        Generated from::

            id: 211
            job: tests/wf-loadContents-job.yml
            label: workflow_input_loadContents_without_inputBinding
            output:
              my_int: 42
            tags:
            - workflow
            - step_input
            - inline_javascript
            - expression_tool
            tool: tests/wf-loadContents2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test WorkflowInputParameter.loadContents""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_expression_tool_input_loadContents(self):
        """Test loadContents on InputParameter.loadContents (expression)

        Generated from::

            id: 212
            job: tests/wf-loadContents-job.yml
            label: expression_tool_input_loadContents
            output:
              my_int: 42
            tags:
            - workflow
            - step_input
            - inline_javascript
            - expression_tool
            tool: tests/wf-loadContents3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test loadContents on InputParameter.loadContents (expression)""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.step_input
    @pytest.mark.inline_javascript
    @pytest.mark.expression_tool
    @pytest.mark.red
    def test_conformance_v1_1_workflow_step_in_loadContents(self):
        """Test WorkflowStepInput.loadContents

        Generated from::

            id: 213
            job: tests/wf-loadContents-job.yml
            label: workflow_step_in_loadContents
            output:
              my_int: 42
            tags:
            - workflow
            - step_input
            - inline_javascript
            - expression_tool
            tool: tests/wf-loadContents4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test WorkflowStepInput.loadContents""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.timelimit
    @pytest.mark.green
    def test_conformance_v1_1_timelimit_basic(self):
        """Test that job fails when exceeding time limit

        Generated from::

            id: 214
            job: tests/empty.json
            label: timelimit_basic
            should_fail: true
            tags:
            - command_line_tool
            - timelimit
            tool: tests/timelimit.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that job fails when exceeding time limit""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.timelimit
    @pytest.mark.green
    def test_conformance_v1_1_timelimit_invalid(self):
        """Test invalid time limit value

        Generated from::

            id: 215
            job: tests/empty.json
            label: timelimit_invalid
            should_fail: true
            tags:
            - command_line_tool
            - timelimit
            tool: tests/timelimit2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test invalid time limit value""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.timelimit
    @pytest.mark.red
    def test_conformance_v1_1_timelimit_zero_unlimited(self):
        """Test zero timelimit means no limit

        Generated from::

            id: 216
            job: tests/empty.json
            label: timelimit_zero_unlimited
            output: {}
            tags:
            - command_line_tool
            - timelimit
            tool: tests/timelimit3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test zero timelimit means no limit""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.timelimit
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_timelimit_from_expression(self):
        """Test expression in time limit

        Generated from::

            id: 217
            job: tests/empty.json
            label: timelimit_from_expression
            should_fail: true
            tags:
            - command_line_tool
            - timelimit
            - inline_javascript
            tool: tests/timelimit4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test expression in time limit""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.expression_tool
    @pytest.mark.timelimit
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_timelimit_expressiontool(self):
        """Test timelimit in expressiontool is ignored

        Generated from::

            id: 218
            job: tests/empty.json
            label: timelimit_expressiontool
            output:
              status: Done
            tags:
            - expression_tool
            - timelimit
            - inline_javascript
            tool: tests/timelimit5.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test timelimit in expressiontool is ignored""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.timelimit
    @pytest.mark.green
    def test_conformance_v1_1_timelimit_basic_wf(self):
        """Test that tool in workflow fails when exceeding time limit

        Generated from::

            id: 219
            job: tests/empty.json
            label: timelimit_basic_wf
            should_fail: true
            tags:
            - workflow
            - timelimit
            tool: tests/timelimit-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that tool in workflow fails when exceeding time limit""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.timelimit
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_timelimit_invalid_wf(self):
        """Test that workflow level time limit is not applied to workflow execution time

        Generated from::

            id: 220
            job: tests/empty.json
            label: timelimit_invalid_wf
            output:
              o: time passed
            tags:
            - workflow
            - timelimit
            - inline_javascript
            tool: tests/timelimit2-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that workflow level time limit is not applied to workflow execution time""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.timelimit
    @pytest.mark.inline_javascript
    @pytest.mark.red
    def test_conformance_v1_1_timelimit_zero_unlimited_wf(self):
        """Test zero timelimit means no limit in workflow

        Generated from::

            id: 221
            job: tests/empty.json
            label: timelimit_zero_unlimited_wf
            output:
              o: time passed
            tags:
            - workflow
            - timelimit
            - inline_javascript
            tool: tests/timelimit3-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test zero timelimit means no limit in workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.workflow
    @pytest.mark.timelimit
    @pytest.mark.inline_javascript
    @pytest.mark.green
    def test_conformance_v1_1_timelimit_from_expression_wf(self):
        """Test expression in time limit in workflow

        Generated from::

            id: 222
            job: tests/empty.json
            label: timelimit_from_expression_wf
            should_fail: true
            tags:
            - workflow
            - timelimit
            - inline_javascript
            tool: tests/timelimit4-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test expression in time limit in workflow""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.networkaccess
    @pytest.mark.red
    def test_conformance_v1_1_networkaccess(self):
        """Test networkaccess enabled

        Generated from::

            id: 223
            job: tests/empty.json
            label: networkaccess
            output: {}
            tags:
            - command_line_tool
            - networkaccess
            tool: tests/networkaccess.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test networkaccess enabled""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.networkaccess
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_networkaccess_disabled(self):
        """Test networkaccess is disabled by default

        Generated from::

            id: 224
            job: tests/empty.json
            label: networkaccess_disabled
            should_fail: true
            tags:
            - networkaccess
            - command_line_tool
            tool: tests/networkaccess2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test networkaccess is disabled by default""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_stage_null_array(self):
        """Test null and array input in InitialWorkDirRequirement

        Generated from::

            id: 225
            job: tests/stage-array-job.json
            label: stage_null_array
            output:
              output:
                basename: lsout
                checksum: sha1$e453d26efd859a9abc80ae1a1d9d63db72376053
                class: File
                location: lsout
                size: 32
            tags:
            - resource
            - command_line_tool
            tool: tests/stage-array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test null and array input in InitialWorkDirRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.resource
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_stage_array_dirs(self):
        """Test array of directories InitialWorkDirRequirement

        Generated from::

            id: 226
            job: tests/stage-array-dirs-job.yml
            label: stage_array_dirs
            output:
              output:
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: a
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: B
                size: 0
            tags:
            - resource
            - command_line_tool
            tool: tests/stage-array-dirs.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test array of directories InitialWorkDirRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.input_object_requirements
    @pytest.mark.red
    def test_conformance_v1_1_cwl_requirements_addition(self):
        """Test requirements in input document via EnvVarRequirement

        Generated from::

            id: 227
            job: tests/env-job3.yaml
            label: cwl_requirements_addition
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - command_line_tool
            - input_object_requirements
            tool: tests/env-tool3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirements in input document via EnvVarRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.input_object_requirements
    @pytest.mark.red
    def test_conformance_v1_1_cwl_requirements_override_expression(self):
        """Test conflicting requirements in input document via EnvVarRequirement and expression

        Generated from::

            id: 228
            job: tests/env-job3.yaml
            label: cwl_requirements_override_expression
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - command_line_tool
            - input_object_requirements
            tool: tests/env-tool4.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test conflicting requirements in input document via EnvVarRequirement and expression""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.input_object_requirements
    @pytest.mark.red
    def test_conformance_v1_1_cwl_requirements_override_static(self):
        """Test conflicting requirements in input document via EnvVarRequirement

        Generated from::

            id: 229
            job: tests/env-job4.yaml
            label: cwl_requirements_override_static
            output:
              out:
                checksum: sha1$715e62184492851512a020c36ab7118eca114a59
                class: File
                location: out
                size: 23
            tags:
            - command_line_tool
            - input_object_requirements
            tool: tests/env-tool3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test conflicting requirements in input document via EnvVarRequirement""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_initial_work_dir_output(self):
        """Test output of InitialWorkDir

        Generated from::

            id: 230
            job: tests/initialworkdirrequirement-docker-out-job.json
            label: initial_work_dir_output
            output:
              OUTPUT:
                checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                class: File
                location: ref.fasta
                secondaryFiles:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: ref.fasta.fai
                  size: 0
                size: 12010
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/initialworkdir-glob-fullpath.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output of InitialWorkDir""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.initial_work_dir
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_glob_full_path(self):
        """Test if full paths are allowed in glob

        Generated from::

            id: 231
            job: tests/initialworkdirrequirement-docker-out-job.json
            label: glob_full_path
            output:
              OUTPUT:
                checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                class: File
                location: ref.fasta
                secondaryFiles:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: ref.fasta.fai
                  size: 0
                size: 12010
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/initialworkdir-glob-fullpath.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test if full paths are allowed in glob""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_fail_glob_outside_output_dir(self):
        """Test fail trying to glob outside output directory

        Generated from::

            id: 232
            job: tests/empty.json
            label: fail_glob_outside_output_dir
            should_fail: true
            tags:
            - required
            - command_line_tool
            tool: tests/glob-path-error.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test fail trying to glob outside output directory""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_symlink_to_file_out_of_workdir_illegal(self):
        """symlink to file outside of working directory should NOT be retrieved

        Generated from::

            id: 233
            job: tests/empty.json
            label: symlink_to_file_out_of_workdir_illegal
            output:
              output_file:
                baesname: symlink.txt
                checksum: sha1$cd28ec34f3f9425aca544b6332453708e8aaa82a
                class: File
                size: 27
            should_fail: true
            tags:
            - command_line_tool
            tool: tests/symlink-illegal.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """symlink to file outside of working directory should NOT be retrieved""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_symlink_to_file_in_workdir_legal(self):
        """symlink to file inside of working directory should be retrieved

        Generated from::

            id: 234
            job: tests/empty.json
            label: symlink-to-file-in-workdir-legal
            output:
              output_file:
                basename: symlink.txt
                checksum: sha1$cd28ec34f3f9425aca544b6332453708e8aaa82a
                class: File
                size: 27
            tags:
            - command_line_tool
            tool: tests/symlink-legal.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """symlink to file inside of working directory should be retrieved""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inplace_update
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_inplace_update_on_file_content(self):
        """inplace update has side effect on file content

        Generated from::

            id: 235
            job: tests/empty.json
            label: inplace_update_on_file_content
            output:
              a: 4
              b: 4
            tags:
            - inplace_update
            - workflow
            tool: tests/inp_update_wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """inplace update has side effect on file content""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.inplace_update
    @pytest.mark.workflow
    @pytest.mark.red
    def test_conformance_v1_1_inplace_update_on_dir_content(self):
        """inplace update has side effect on directory content

        Generated from::

            id: 236
            job: tests/empty.json
            label: inplace_update_on_dir_content
            output:
              a:
              - basename: blurb
                class: File
                location: blurb
              b:
              - basename: blurb
                class: File
                location: blurb
            tags:
            - inplace_update
            - workflow
            tool: tests/inpdir_update_wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """inplace update has side effect on directory content""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_outputbinding_glob_directory(self):
        """Test that OutputBinding.glob accepts Directories

        Generated from::

            id: 237
            job: tests/empty.json
            label: outputbinding_glob_directory
            output:
              directories:
              - basename: a_dir
                class: Directory
                listing: []
              - basename: b_dir
                class: Directory
                listing: []
              - basename: c_dir
                class: Directory
                listing: []
            tags:
            - required
            - command_line_tool
            tool: tests/glob_directory.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that OutputBinding.glob accepts Directories""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_stage_file_array_to_dir(self):
        """Test that array of input files can be staged to directory with entryname

        Generated from::

            id: 238
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that array of input files can be staged to directory with entryname""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_stage_file_array_to_dir_basename(self):
        """Test that array of input files can be staged to directory with basename

        Generated from::

            id: 239
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir_basename
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array_basename.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that array of input files can be staged to directory with basename""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_stage_file_array_to_dir_basename_entryname(self):
        """Test that if array of input files are staged to directory with basename and entryname, entryname overrides

        Generated from::

            id: 240
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir_basename_entryname
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array_basename_and_entryname.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that if array of input files are staged to directory with basename and entryname, entryname overrides""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_tmpdir_is_not_outdir(self):
        """Test that runtime.tmpdir is not runtime.outdir

        Generated from::

            id: 241
            job: tests/empty.json
            label: tmpdir_is_not_outdir
            output:
              foo:
                basename: foo
                checksum: sha1$fa98d6085770a79e44853d575cd3ab40c0f1f4de
                class: File
            tags:
            - command_line_tool
            tool: tests/runtime-paths-distinct.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that runtime.tmpdir is not runtime.outdir""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_listing_default_none(self):
        """Test that default behavior is 'no_listing' if not specified

        Generated from::

            id: 242
            job: tests/listing-job.yml
            label: listing_default_none
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_none1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that default behavior is 'no_listing' if not specified""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_listing_requirement_none(self):
        """Test that 'listing' is not present when LoadListingRequirement is 'no_listing'

        Generated from::

            id: 243
            job: tests/listing-job.yml
            label: listing_requirement_none
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_none2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is not present when LoadListingRequirement is 'no_listing'""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_listing_loadListing_none(self):
        """Test that 'listing' is not present when loadListing on input parameter is 'no_listing'

        Generated from::

            id: 244
            job: tests/listing-job.yml
            label: listing_loadListing_none
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_none3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is not present when loadListing on input parameter is 'no_listing'""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_listing_requirement_shallow(self):
        """Test that 'listing' is present in top directory object but not subdirectory object when LoadListingRequirement is 'shallow_listing'


        Generated from::

            id: 245
            job: tests/listing-job.yml
            label: listing_requirement_shallow
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_shallow1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is present in top directory object but not subdirectory object when LoadListingRequirement is 'shallow_listing'
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_listing_loadListing_shallow(self):
        """Test that 'listing' is present in top directory object but not subdirectory object when loadListing on input parameter loadListing is 'shallow_listing'


        Generated from::

            id: 246
            job: tests/listing-job.yml
            label: listing_loadListing_shallow
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_shallow2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is present in top directory object but not subdirectory object when loadListing on input parameter loadListing is 'shallow_listing'
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_listing_requirement_deep(self):
        """Test that 'listing' is present in top directory object and in subdirectory objects when LoadListingRequirement is 'deep_listing'


        Generated from::

            id: 247
            job: tests/listing-job.yml
            label: listing_requirement_deep
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_deep1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is present in top directory object and in subdirectory objects when LoadListingRequirement is 'deep_listing'
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_listing_loadListing_deep(self):
        """Test that 'listing' is present in top directory object and in subdirectory objects when input parameter loadListing is 'deep_listing'


        Generated from::

            id: 248
            job: tests/listing-job.yml
            label: listing_loadListing_deep
            output:
              out: true
            tags:
            - command_line_tool
            tool: tests/listing_deep2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that 'listing' is present in top directory object and in subdirectory objects when input parameter loadListing is 'deep_listing'
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.green
    def test_conformance_v1_1_inputBinding_position_expr(self):
        """Test for expression in the InputBinding.position field; also test using emoji in CWL document and tool output


        Generated from::

            id: 249
            job: tests/echo-position-expr-job.yml
            label: inputBinding_position_expr
            output:
              out: "\U0001F57A 1 singular sensation!\n"
            tags:
            - command_line_tool
            - required
            tool: tests/echo-position-expr.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test for expression in the InputBinding.position field; also test using emoji in CWL document and tool output
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.command_line_tool
    @pytest.mark.required
    @pytest.mark.red
    def test_conformance_v1_1_outputEval_exitCode(self):
        """Can access exit code in outputEval

        Generated from::

            id: 250
            job: tests/empty.json
            label: outputEval_exitCode
            output:
              code: 7
            tags:
            - command_line_tool
            - required
            tool: tests/exitcode.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Can access exit code in outputEval""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_any_input_param_graph_no_default(self):
        """Test use of $graph without specifying which process to run

        Generated from::

            id: 251
            job: tests/env-job.json
            label: any_input_param_graph_no_default
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool-packed.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of $graph without specifying which process to run""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.command_line_tool
    @pytest.mark.red
    def test_conformance_v1_1_any_input_param_graph_no_default_hashmain(self):
        """Test use of $graph without specifying which process to run, hash-prefixed "main"


        Generated from::

            id: 252
            job: tests/env-job.json
            label: any_input_param_graph_no_default_hashmain
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool-packed2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of $graph without specifying which process to run, hash-prefixed "main"
""")

    @pytest.mark.cwl_conformance
    @pytest.mark.cwl_conformance_v1_1
    @pytest.mark.required
    @pytest.mark.inline_javascript
    @pytest.mark.command_line_tool
    @pytest.mark.green
    def test_conformance_v1_1_optional_numerical_output_returns_0_not_null(self):
        """Test that optional number output is returned as 0, not null


        Generated from::

            id: 253
            job: tests/empty.json
            label: optional_numerical_output_returns_0_not_null
            output:
              out: 0
            tags:
            - required
            - inline_javascript
            - command_line_tool
            tool: tests/optional-numerical-output-0.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that optional number output is returned as 0, not null
""")
