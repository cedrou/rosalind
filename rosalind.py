def ReadFasta(fasta):
    import re
    return {match.group(1):match.group(2).replace('\n','') for match in re.finditer(">([^\n]+)\n([^>]*)", fasta)}

