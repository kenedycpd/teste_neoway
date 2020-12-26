
import urllib2
import urllib
import re
import sys
import csv


url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
valores = {'relaxation': sys.argv[1],
           'tipoCep': 'ALL',
           'semelhante': 'N'}

dados = urllib.urlencode(valores)
httpRequest = urllib2.Request(url, dados)
httpResponse = urllib2.urlopen(httpRequest)
html = httpResponse.read()

extrai = r"(?:<td.*?>)(.*?)(?:</td>)"

resultado = re.findall(extrai, html)
print 'Logradouro.............', resultado[0]
print 'Bairro.............', resultado[1]
print 'Localidade-UF.............', resultado[2]
print 'Cep.............', resultado[3]

f = open('tabela.csv', 'a')
escreve = csv.writer(f)
escreve.writerow(resultado)
