(Stage_1) -> (Stage_2) -> (Stage_3)

Command => PipelineManager (has many handlers / do_pipeline(): Execute handlers) => Handler(interface: do_process) -> Many Handler


* Command: command object to be process. A tweet in our example
* PipelineManager: central class of the pattern. Define the following attribute and method
** handlers: list (ordered) of Handlers
** doPipeline(Command object): execute the processing pipeline
* Handler: an interface defining the process(Command object) method
