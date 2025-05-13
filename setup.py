import setuptools

setuptools.setup(
    name="extension_rvc",
    packages=setuptools.find_namespace_packages(),
    version="0.0.3",
    author="rsxdalv",
    description="RVC: Retrieval-based Voice Conversion",
    url="https://github.com/rsxdalv/extension_rvc",
    project_urls={},
    scripts=[],
    install_requires=[
        "rvc @ https://github.com/rsxdalv/Retrieval-based-Voice-Conversion/releases/download/v0.3.6/rvc-0.3.6-py3-none-any.whl",
        "torchfcpe",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
