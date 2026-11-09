# HelloActions-MerveFilizBaker
### Workflow Test!

## Explain the Workflow

29. **What is the purpose of the on section?**  
    It defines the events such as a push or manual trigger that automatically or manually initiate the execution of the workflow.

30. **What does workflow_dispatch do?**  
    It enables manual execution of the workflow directly from the GitHub web interface (Actions tab).

31. **What does runs-on specify?**  
    It specifies the type of virtual machine runner environment where the job will be executed.

32. **Why is actions/checkout needed?**  
    It clones the repository's source code onto the runner so that the workflow has access to the project files.

33. **What does the language setup action do?**  
    It installs and configures the specific programming language version and its tooling environment on the runner.

34. **What is the difference between compiling and running the program?**  
    Compiling translates human-readable source code into machine-executable binary code before execution, whereas running executes the code directly.

35. **Where can you see the program output?**  
    In the GitHub Actions run logs under the specific step inside the repository's Actions tab.

36. **What is the difference between a workflow, a job, and a step?**  
    * Workflow: An automated procedure defined in a YAML file that contains one or more jobs.
    * Job: A set of execution steps that run on the same virtual machine runner.
    * Step: An individual task or shell command executed sequentially within a job.
