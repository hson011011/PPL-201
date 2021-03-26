from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
    				CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])

    

