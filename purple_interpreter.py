import purple_lexer
import purple_parser

#Menafsirkan adalah prosedur sederhana. Ide dasarnya adalah untuk mengambil pohon 
#dan berjalan melaluinya dan mengevaluasi operasi aritmatika secara hierarkis. 
#Proses ini secara rekursif dipanggil berulang kali sampai seluruh pohon dievaluasi dan jawabannya diambil.

class PurpleExecute:
    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] = '"':
            print(result)

    def walkTree(self, node):
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if none is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])
        
        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]
        
        if node[0] == 'print':
            if node[1][0] = '"':
                print(node[1][1:len(node[1])-1])
            else:
                return self.walkTree(node[1])
        
        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])
        
        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

        if node[0] == 'fun_def':
            self.env[node[1]] = node[2]
        
        if node[0] == 'fun_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Undefined function '%s" % node[1])
                return 0