{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports\n",
    "from requests import get\n",
    "from bs4 import BeautifulSoup\n",
    "import html5lib\n",
    "import re\n",
    "from yaml import dump\n",
    "\n",
    "# requisitando as informações do site correspondente a url\n",
    "response = get(\"https://www.w3schools.io/file/yaml-sample-example/\")\n",
    "\n",
    "# criando um objeto python do tipo beautifulSoup, que recebe o conteudo do site formatado em texto, e um parset para podermos trabalhar com as tags html \n",
    "soup = BeautifulSoup(response.text, \"html5lib\")\n",
    "\n",
    "# procurando o conteudo de uma tag dentro do html e atribuindo esse conteudo a variavel \"exemple\" \n",
    "exemple = soup.find(\"pre\")\n",
    "\n",
    "# limpando o conteudo (retirando as tegs html)\n",
    "exemple = exemple.text \n",
    "\n",
    "# no trecho abaixo \n",
    "# crio um arquivo\n",
    "# atribuo conteudo a ele\n",
    "# o fecho \n",
    "# OBS, não usei 'w+' pois causa complicações  \n",
    "oldfile = open(\"oldfile.txt\", 'w')\n",
    "oldfile.write(exemple)\n",
    "oldfile.close()\n",
    "\n",
    "# o abro em modo de leitura para que o loop \"for\" possa interagir com ele\n",
    "oldfile = open(\"oldfile.txt\", 'r')\n",
    "\n",
    "# crio outro arquivo\n",
    "newfile = open(\"newfile.yml\", 'w')\n",
    "\n",
    "# leio o arquivo que guarda o conetudo escolido do site\n",
    "for line in oldfile:            \n",
    "\n",
    "    # procuro em cada linha do arquivo o char \"#\"\n",
    "    if \"#\" in line:  \n",
    "        # aplico um regex para deletar o char e tudo que vem depois até a quebra de linha\n",
    "        l = re.sub(r'#.*$', '', line)\n",
    "        # guardo a linha limpa de comentario no novo arquivo\n",
    "        newfile.write(l)\n",
    "\n",
    "    else:\n",
    "        # guardo a linha que originalmente ja não possuia nenhum comentario\n",
    "        newfile.write(line)\n",
    "        \n",
    "oldfile.close()\n",
    "newfile.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
