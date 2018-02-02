# SUD
Syntactic Universal Dependency Treebanks

The conll folder contains the UD treebanks that have been transformed to functional heads.
The tool folder contains tools that were used for the transformation: 
- conlleva can transform individual treebanks and create html views
- syntacticize applies the grammar in parallel and only produces the final conllu files.

Conlleva. (it leads to, it puts up with)

Usage:
  conlleva.py tohtml <conllu_file>
  conlleva.py search <conllgrammar_file> <conllu_file> [--includeNonMatchingTrees]
  conlleva.py transform <transconllgrammar_file> <conllu_file> [--addStat]
  conlleva.py (-h | --help)
  conlleva.py (-v | --version)

Options:
  -h --help  Show this screen.
  -v --version  Show version.
  -i --includeNonMatchingTrees  include non-matching trees in the output file of search
  -a --addStat  add statistics in the output file of transform

Example Uses:
python3 conlleva.py tohtml "fr_sequoia-ud-test.conllu"
python3 conlleva.py search search.udauxaux.conllu fr_sequoia-ud-test.conllu --includeNonMatchingTrees
python3 conlleva.py transform UDtoSUD.txt fr_sequoia-ud-test.conllu --addStat

