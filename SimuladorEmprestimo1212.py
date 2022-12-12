#Desafio junior Simulador de Emprestimo
while True:
    print("--------------------------------------------------")
    print(" Seja bem-vindo(a)  ao Mybank ")
    print(" SIMULADOR DE  EMPRESTIMO  ")
    print("--------------------------------------------------")
    resposta  = input("Voce é nosso  Cliente?s/n: ")
    emprestimo  = int(input("  valor desejado  para  o  emprestimo:"))
    parcelas = int(input("Quantidade  de parcelas:"))
    SeguroDesemprego = input("Deseja incluir um seguro Desemprego?s/n:  ")
    if  resposta == 'n':
        Score  = int(input("Digite seu Serasa Score:"))
        while Score <  0:
                    print("Score inválido!")
                    Score = int(input("Informe  novamente seu Score:"))
        if Score   == 0 or Score   <=  299:
                valorFinal   =  emprestimo * 1.2 *1.0038 + 35
                juros  =   20
                if SeguroDesemprego == 's':
                        valorFinal   =  emprestimo * 1.2 *1.0038*1.035 + 35
        elif  Score > 299  and Score <= 499:
                    valorFinal   =  emprestimo * 1.15 *1.0038 + 35
                    juros = 15
                    if SeguroDesemprego == 's':
                        valorFinal   =  emprestimo * 1.15 *1.0038*1.035 + 35
        elif  Score  > 499  and  Score  <=  699:
                valorFinal =  emprestimo*1.1*1.0038 + 35
                juros = 10
                if SeguroDesemprego == 's':
                        valorFinal   =  emprestimo * 1.1 *1.0038*1.035 + 35
        else:
                valorFinal  = emprestimo *  1.05*1.0038 + 35
                juros = 5
                if SeguroDesemprego == 's':
                        valorFinal   =  emprestimo * 1.05 *1.0038*1.035 + 35  
    else:
        valorFinal = emprestimo  * 1.04*1.0038
        juros = 4
        if SeguroDesemprego == 's':
            valorFinal   =  emprestimo * 1.04 *1.0038*1.035
    valorParcela = valorFinal/parcelas
    print("------------------------------------------")
    print("Resultado  da Simulação")
    print("------------------------------------------")
    print(f"Quantidade de Parcelas: {parcelas} ")
    print(f"Valor das Parcelas: {valorParcela:.2f} ")
    print(f"Taxa de   juros:{juros}%")
    print(f"Custo efetivo  total: {valorFinal:.2f}")
    print("------------------------------------------")
    simular = input("Deseja  realizar outra Simulação?s/n:")
    print("Programa  Encerrado")
    if simular == 'n':
        break


        
    
                    
        
     
            
          
                         
 
                 
        
              
       
               
                     
                                        
                      
                  

          
               
           
               
              
   
               
          
             
            


             





    
     
    




    
    
    
    

    
             


             

             

