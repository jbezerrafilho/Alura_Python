class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        return self._codigo == other._codigo


conta1 = ContaSalario(1)
conta2 = ContaSalario(1)
var = conta2 == conta1
print(var)
