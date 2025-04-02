from crewai.tools import tool, BaseTool
from pydantic import BaseModel, Field
from typing import Type

class CalculationInputSchema(BaseModel):
    operation: str = Field(..., description="The mathematical operation to perform")
    factor: float = Field(..., description="A factor by which to multiply the result of the operation")
    

class CalculatorTools(BaseTool):

    name: str = "Evaluate mathematic expressions"
    description: str = "A tool that can be used to evaluate mathematical expressions presented as strings"
    args_schema: Type[BaseModel] = CalculationInputSchema
    
    def _run(self, operation: str, factor:  float):
        
        result = eval(operation) * factor
        
        return f"The result of {operation}, multiplied by {factor} is {result}."

#     @tool("Make a calculation")
#     def calculate(self, operation):
#         """Useful to perform any mathematical calculations,
#         like sum, minus, multiplication, division, etc.
#         The input to this tool should be a mathematical
#         expression, a couple examples are `200*7` or `5000/2*10`
#         """
#         try:
#             return eval(operation)
#         except SyntaxError:
#             return "Error: Invalid syntax in mathematical expression"
