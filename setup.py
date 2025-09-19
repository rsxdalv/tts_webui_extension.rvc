import setuptools

setuptools.setup(
    name="tts_webui_extension.rvc",
    packages=setuptools.find_namespace_packages(),
    version="0.0.4",
    author="rsxdalv",
    description="RVC: Retrieval-based Voice Conversion",
    url="https://github.com/rsxdalv/tts_webui_extension.rvc",
    project_urls={},
    scripts=[],
    install_requires=[
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp310-cp310-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.10'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.10'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp310-cp310-macosx_11_0_universal2.whl ; sys_platform == 'darwin' and python_version == '3.10'",

        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp311-cp311-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.11'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.11'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp311-cp311-macosx_11_0_universal2.whl ; sys_platform == 'darwin' and python_version == '3.11'",

        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp312-cp312-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.12'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.12'",
        "fairseq @ https://github.com/rsxdalv/fairseq/releases/download/v0.12.3/fairseq-0.12.13-cp312-cp312-macosx_11_0_universal2.whl ; sys_platform == 'darwin' and python_version == '3.12'",

        "rvc @ https://github.com/rsxdalv/Retrieval-based-Voice-Conversion/releases/download/v0.3.6/rvc-0.3.6-py3-none-any.whl",
        "torchfcpe",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

