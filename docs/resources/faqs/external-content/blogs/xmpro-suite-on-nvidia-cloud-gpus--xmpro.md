# XMPro Suite on NVIDIA Cloud GPUs - XMPRO

{% embed url="https://xmpro.com/xmpro-suite-on-nvidia-cloud-gpus/" %}

This week XMPro announced that it has become an NVIDIA Cloud-Validated partner. By using the NVIDIA AI platform, we are better positioned to support customers to bridge the gap between data flow and operational AI in the cloud.
To get here, we completed a rigorous test plan to validate and showcase the XMPro Suite running efficiently on NVIDIA’s technology stack. This included building an agent to process a sample AI workload using NVIDIA GPUs (via CUDA) to showcase how the XMPro suite runs optimally on the NVIDIA stack.
And how did we do this, you ask? The following steps outline the process we used to test XMPro on an NVIDIA GPU.

Step One: Build an Agent – Follow our docs to build and package an Agent. Import your preferred CUDA NuGet package when building your agent. In this example we used ILGPU.
You can find a list of popular libraries in NuGet.
Step Two: Provision an NVIDIA GPU service in the cloud – Provision your preferred NVIDIA Virtual Machine Image and cloud provider.
Step Three: Install Stream Host – Follow the docs to install the XMPro Stream Host on Ubuntu 20.04 using the provisioned virtual machine in step two.
Step Four: Add the Agent to a Stream – Import an agent, add to a stream, configure the agent and publish the stream. 
The primary objective of NVIDIA cloud validation is to help customers easily identify and adopt validated NVIDIA-based solutions. XMPro is now part of the NVIDIA Accelerated Applications Catalog, which features world-class GPU- and DPU-accelerated solutions.
About Daniel King: Daniel King is Development Manager for XMPro, with 19 years of experience in development and solution architecture. He designs simple solutions to complex problems that deliver business value.