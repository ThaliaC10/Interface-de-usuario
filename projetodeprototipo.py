Goldwing - Interface Premium para Agendamento e Portfólio de Maquiagem Artística com Python & Tkinter

Este é um projeto passo a passo estruturado em 5 etapas progressivas para construir uma interface moderna e elegante para a marca Goldwing, especializada em maquiagem artística e criativa.
Desenvolvido inteiramente com a biblioteca padrão Tkinter do Python, este projeto implementa conceitos modernos de design minimalista, estética sofisticada inspirada em asas e luz, animações suaves, formulários interativos e validações intuitivas.
Todas as variáveis e funções foram nomeadas em português, tornando o aprendizado mais acessível e didático.

#Paleta de Cores e Estética

Inspirada na identidade visual da Goldwing e na delicadeza das mariposas.

Fundo Principal (Janela): #faf7f5 (Off White Elegante)
Fundo do Painel: #ffffff (Branco Suave)
Campos de Entrada: #f3eef8 (Lavanda Muito Clara)
Destaque Primário: #8b5cf6 (Violeta Goldwing)
Destaque Secundário: #c084fc (Lilás Luminoso)
Texto Principal: #2d2d2d (Cinza Escuro Sofisticado)
Texto Secundário / Placeholders: #8c8c99
Mensagem de Erro: #e63946
Mensagem de Sucesso: #52b788
Detalhes Decorativos: #d8b4fe (Lilás Pastel)
🦋 Conceito Visual

Inspirado pelas asas delicadas das mariposas, cada elemento da interface transmite leveza, criatividade e liberdade artística.

A experiência do usuário busca refletir a essência da Goldwing:

"Onde a maquiagem se transforma em arte."

#Estrutura das Etapas

Cada arquivo representa uma fase do desenvolvimento, construindo a interface gradualmente.

1. etapa_1_estrutura.py
Configura a janela principal (1000x600px).
Impede redimensionamentos para preservar a composição visual.
Centraliza automaticamente a aplicação na tela.
Divide a interface em:
painel_esquerdo para ilustração artística.
painel_direito para login e navegação.
2. etapa_2_visual.py
Carrega a arte principal inspirada em maquiagem criativa.
Exibe a marca Goldwing em destaque.
Adiciona o slogan:

"Soft beauty inspired by light and wings"

Cria elementos visuais suaves utilizando Canvas Tkinter.
3. etapa_3_campos.py
Cria campos personalizados para:
Nome
E-mail
Senha
Implementa placeholders animados:
ao_focar_nome
ao_desfocar_nome
ao_focar_email
ao_desfocar_email
Utiliza contêineres modernos simulando bordas arredondadas.
4. etapa_4_botoes.py

Adiciona o botão principal:

"Entrar no Universo Goldwing"

Adiciona links:
"Esqueceu sua senha?"
"Criar Conta"
Implementa efeitos de hover suaves:
ao_passar_mouse_botao
ao_sair_mouse_botao
Adiciona animações visuais inspiradas em luz e movimento.
5. etapa_5_completo.py
Implementa autenticação completa.
Valida preenchimento obrigatório dos campos.
Verifica formato de e-mail usando Regex.
Exibe mensagens visuais elegantes através da função:
mostrar_feedback()
Destaca campos incorretos usando:
destacar_campo()
Permite envio através:
Do botão de login.
Da tecla ENTER.
Exibe mensagens personalizadas da Goldwing:
"Bem-vinda ao universo Goldwing ✨"
"Preencha todos os campos para continuar."
"E-mail inválido."
✨ Funcionalidades Extras
Modo claro sofisticado.
Animações suaves de foco.
Design inspirado em arte e beleza criativa.
Integração com portfólio de maquiagens.
Área para exibição de trabalhos recentes.
Links para redes sociais:
Instagram: @goldwing_makeup
TikTok: @goldwingmakeup
Pinterest: @makeupgoldwing
🦋 Filosofia da Marca

"Inspirado pelas asas delicadas das mariposas, cada maquiagem nasce da liberdade de criar algo único."

Goldwing — Arte que Transforma Sentimentos. ✨🦋
