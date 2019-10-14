import csv
import sys

def tabula(csvfile, innersep=', '):
    '''
    Counts and agreggates data in a csv file. Multiple value fields will be split by innersep pattern.
    '''

    r=list(csv.reader(csvfile))
    headers=r.pop(0)

    results={}
    for h in headers:
        results[h]={}

    for l in list(r)[1:]:
        for i in range(len(l)):
            innervals=l[i].split(innersep)
            for s in innervals:
                if not s in results[headers[i]]:
                    results[headers[i]][s]=0
                results[headers[i]][s]+=1

    return headers, results


def graph(resultados):
    retorno = ""
    maximo=max(resultados.values())
    maxlen=max([len(i) for i in resultados])
    for escolha, valor in resultados.items():
        retorno += '%s %i %s\n' % (
            escolha.ljust(maxlen),
            valor,
            '|' * int(50*valor/maximo)
        )
    return retorno

if __name__ == '__main__':
    if '-t' in sys.argv:
        import json
        headers,data=tabula(open('sample/sample.csv'))
        cheaders=json.load(open('sample/sampleheaders.json'))
        cdata=json.load(open('sample/sampledata.json'))
        assert headers==cheaders
        assert data==cdata
    else:
        headers,data=tabula(open(sys.argv[1]))
        for i in headers[4:8]:
            print(i)
            print(graph(data[i]))


