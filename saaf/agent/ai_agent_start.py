class Ai_agent:
    def __ini__(self):
        self.memory = []
    
    def Think(self,user_input):
        """
        LLM will decide what to do
        (For now we simulate it)
        """
        
        if "multiply" in user_input or "*" in user_input :
            return "use_tool:calculator"
        else:
            return "direct answer"
    
    def act(self,decision,user_input):
         if decision == 'use_tool:calculator':
             return self.calculator(user_input)
         else:
             return "i will answer directly " + user_input
    def calculator(self,user_input):
       try:
          return eval(user_input)
       except:
           return "Error in calculation"
    
         
    def run(self,user_input):
        decision = self.Think(user_input)
        result   = self.act(decision,user_input)
        return result
    
agent = Ai_agent() 

while True:
    user_input = input("\n You:")
    output = agent.run(user_input)
    print('Agent:',output)
    if  "exit" in user_input.lower():
        break
    
                
          
        
        