===========
JAM Project
===========

``JAM Project`` はPythonで書かれた、日本語文章の文法チェックツールです。

「きれいな日本語reSTを書きやすくする」ことをサポートすることが、このツールの目的となります。

.. note::

    このドキュメントは未来の目標を含みます。
    ToDoや注釈の分量が当面の間多いものと考えてください。


使い始めるまで
==============

必要な環境
----------

* Python 3.7+ インタプリタ環境

インストール
------------

現状はPyPI登録をしていないため、GitHubのアーカイブを直接インストルする形式となります。

.. code-block:: bash

    $ pip install https://github.com/attakei/jamproject.git


使い方
======

単文の直接チェック
------------------

.. code-block:: bash

    $ jamt 今日はいい天気でした。

ファイルの行単位チェック
------------------------

.. code-block:: bash

    $ jam --line index.rst


reSTファイルの文章単位チェック
------------------------------

.. code-block:: bash

    $ jam index.rst

ディレクトリ全体のチェック
--------------------------

.. code-block:: bash

    $ jam docs/

