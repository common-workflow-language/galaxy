#!/usr/bin/env cwl-runner
class: CommandLineTool
cwlVersion: "cwl:draft-3"
description: "Print the contents of a file to stdout using 'cat' running in a docker container."
hints:
  - class: DockerRequirement
    dockerPull: debian:wheezy
inputs:
  - id: file1
    type: File
    default:
      class: File
      path: hello.txt
    label: Input File
    description: "The file that will be copied using 'cat'"
    inputBinding: {position: 1}
outputs:
  - id: output_file
    type: File
    outputBinding: {glob: output.txt}
baseCommand: cat
stdout: output.txt