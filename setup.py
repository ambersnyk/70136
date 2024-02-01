# Copyright (c) 2023 Synthesia Limited - All Rights Reserved
#
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

from setuptools import find_packages, setup

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=True,
    install_requires=[
        "synthesia-datalib>=1.5.0",
        "synthesia-rnd-masksandmattes>=0.1.3",
        "typer>=0.9.0",
        "diffusers>=0.21.2",
        "torch>=2.0.0",
        "transformers>=4.28.1",
        "xformers>=0.0.20",
        "accelerate>=0.17.0",
        "scikit-image>=0.22.0",
        # Pin versions to address security CVEs
        "urllib3>=1.26.18",
        "pillow>=10.0.1",
    ],
    extras_require={
        "dev": [
            "black>=23.1",
            "click~=8.1",
            "pip-tools~=6.12",
            "pytest~=7.2",
            "pre-commit>=2.21,<4.0",
            "ruff~=0.0",
            "build~=0.10",
        ],
    },
    include_package_data=True,
)
