Additional Features
===================

Additional features in *Inference System for Selecting the Optimal Programming Language* project.

Self-generating Documentation
-----------------------------

Self-generating documentation after every merge to the `main` branch.
It uses the `Sphinx` framework and the `Furo` theme.

Link for GitHub Action -> |self_generating_documentation|

----------------------

Pipelines
---------

Link for GitHub Action -> |pipeline|

----------------------

Tests pipeline
++++++++++++++

After each push from dev or main branch, a pipeline using the `pytest` framework automatically run all tests.
If all tests do not pass on the dev branch, it will not be possible to merge changes to the main branch.

----------------------

Code Formatter pipeline
+++++++++++++++++++++++

After each push from dev or main branch, a pipeline using the `black` framework automatically formats the code
according to PEP 8 standards. The formatted changes are committed and pushed to the used branch.


.. |self_generating_documentation| raw:: html

   <a href="https://github.com/Wolanin00/Inference-System-for-Selecting-the-Optimal-Programming-Language/actions/workflows/pages/pages-build-deployment" target="_blank">Self-generating Documentation</a>

.. |pipeline| raw:: html

   <a href="https://github.com/Wolanin00/Inference-System-for-Selecting-the-Optimal-Programming-Language/actions/workflows/pipeline.yml" target="_blank">Pipeline</a>
