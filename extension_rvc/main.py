import gradio as gr
from .rvc_tab import rvc_ui


def extension__tts_generation_webui():
    rvc_ui()
    return {
        "package_name": "extension_rvc",
        "name": "RVC",
        "version": "0.0.2",
        "requirements": "git+https://github.com/rsxdalv/extension_rvc@main",
        "description": "RVC: Retrieval-based Voice Conversion",
        "extension_type": "interface",
        "extension_class": "audio-conversion",
        "author": "RVC Team",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI",
        "extension_website": "https://github.com/rsxdalv/extension_rvc",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        demo.close()  # type: ignore
    with gr.Blocks(analytics_enabled=False) as demo:
        rvc_ui()

    demo.launch(
        server_port=7770,
    )
