# Este exemplo apresenta uma aplicação completa de OpenGL, que renderiza um quadrado e um triângulo na tela.
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm = None
Vao_quadrado1 = None
Vao_quadrado2 = None
Vao_quadrado3 = None
Vao_quadrado4 = None
Vao_quadrado5 = None
Vao_quadrado6 = None
Vao_triangulo1 = None
Vao_triangulo2 = None
Vao_triangulo3 = None
WIDTH = 800
HEIGHT = 600

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaTriangulo1():
    global Vao_triangulo1

    # VAO do triângulo
    Vao_triangulo1 = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo1)

    # VBO dos vértices
    points = [
		-0.1, -0.75, 0.0, #cima
		-0.4, -0.65, 0.0, #direita
		-0.4, -0.85, 0.0 #/esquerda
	]

    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		0.0, 0.5, 0.0, #vermelho
		0.0, 0.5, 0.0, #verde
		0.0, 0.5, 0.0  #azul
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaTriangulo2():
    global Vao_triangulo2

    # VAO do triângulo
    Vao_triangulo2 = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo2)

    # VBO dos vértices
    points = [
		-0.1, 0.75, 0.0, #cima
		-0.4, 0.85, 0.0, #direita
		-0.4, 0.65, 0.0 #/esquerda
	]

    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		0.0, 0.5, 0.0, #vermelho
		0.0, 0.5, 0.0, #verde
		0.0, 0.5, 0.0  #azul
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaTriangulo3():
    global Vao_triangulo3

    # VAO do triângulo
    Vao_triangulo3 = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo3)

    # VBO dos vértices
    points = [
		0.0, 0.0, 0.0, #cima
		-0.4, 0.45, 0.0, #direita
		-0.4, -0.45, 0.0 #/esquerda
	]

    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		0.8, 0.0, 0.0, #vermelho
		0.8, 0.0, 0.0, #verde
		0.8, 0.0, 0.0  #azul
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado1():
    global Vao_quadrado1
    # Vao do quadrado
    Vao_quadrado1 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado1)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		-0.8, 1.0, 0.0, #vertice superior direito
		-1.0, 1.0, 0.0, #vertice inferior direito
		-1.0, -1.0, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.8, -1.0, 0.0, #vertice superior esquerdo
		-0.8, 1.0, 0.0, #vertice superior direito
		-1.0, -1.0, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.0, 0.7, 0.0,#amarelo
		0.0, 0.7, 0.0,#ciano
		0.0, 0.7, 0.0,#magenta
		#triângulo 2
		0.0, 0.7, 0.0,#ciano
		0.0, 0.7, 0.0,#amarelo
		0.0, 0.7, 0.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado2():
    global Vao_quadrado2
    # Vao do quadrado
    Vao_quadrado2 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado2)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		-0.4, -0.7, 0.0, #vertice superior direito
		-0.8, -0.7, 0.0, #vertice inferior direito
		-0.8, -0.8, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.4, -0.8, 0.0, #vertice superior esquerdo
		-0.4, -0.7, 0.0, #vertice superior direito
		-0.8, -0.8, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.5, 0.2, 0.0,#amarelo
		0.5, 0.2, 0.0,#ciano
		0.5, 0.2, 0.0,#magenta
		#triângulo 2
		0.5, 0.2, 0.0,#ciano
		0.5, 0.2, 0.0,#amarelo
		0.5, 0.2, 0.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado3():
    global Vao_quadrado3
    # Vao do quadrado
    Vao_quadrado3 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado3)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		-0.4, 0.8, 0.0, #vertice superior direito
		-0.8, 0.8, 0.0, #vertice inferior direito
		-0.8, 0.7, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.4, 0.7, 0.0, #vertice superior esquerdo
		-0.4, 0.8, 0.0, #vertice superior direito
		-0.8, 0.7, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.5, 0.2, 0.0,#amarelo
		0.5, 0.2, 0.0,#ciano
		0.5, 0.2, 0.0,#magenta
		#triângulo 2
		0.5, 0.2, 0.0,#ciano
		0.5, 0.2, 0.0,#amarelo
		0.5, 0.2, 0.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado4():
    global Vao_quadrado4
    # Vao do quadrado
    Vao_quadrado4 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado4)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		-0.4, 0.4, 0.0, #vertice superior direito
		-0.8, 0.4, 0.0, #vertice inferior direito
		-0.8, -0.4, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.4, -0.4, 0.0, #vertice superior esquerdo
		-0.4, 0.4, 0.0, #vertice superior direito
		-0.8, -0.4, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		1.0, 0.9, 0.8,#amarelo
		1.0, 0.9, 0.8,#ciano
		1.0, 0.9, 0.8,#magenta
		#triângulo 2
		1.0, 0.9, 0.8,#ciano
		1.0, 0.9, 0.8,#amarelo
		1.0, 0.9, 0.8,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado5():
    global Vao_quadrado5
    # Vao do quadrado
    Vao_quadrado5 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado5)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		-0.7, 0.1, 0.0, #vertice superior direito
		-0.8, 0.1, 0.0, #vertice inferior direito
		-0.8, -0.1, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.7, -0.1, 0.0, #vertice superior esquerdo
		-0.7, 0.1, 0.0, #vertice superior direito
		-0.8, -0.1, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.5, 0.1, 0.0,#amarelo
		0.5, 0.1, 0.0,#ciano
		0.5, 0.1, 0.0,#magenta
		#triângulo 2
		0.5, 0.1, 0.0,#ciano
		0.5, 0.1, 0.0,#amarelo
		0.5, 0.1, 0.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado6():
    global Vao_quadrado6
    # Vao do quadrado
    Vao_quadrado6 = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado6)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		1.0, -0.6, 0.0, #vertice superior direito
		0.6, -0.6, 0.0, #vertice inferior direito
		0.6, -1.0, 0.0, #vertice inferior esquerdo
		#triângulo 2
		1.0, -1.0, 0.0, #vertice superior esquerdo
		1.0, -0.6, 0.0, #vertice superior direito
		0.6, -1.0, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		1.0, 1.0, 0.0,#amarelo
		1.0, 1.0, 0.0,#ciano
		1.0, 1.0, 0.0,#magenta
		#triângulo 2
		1.0, 1.0, 0.0,#ciano
		1.0, 1.0, 0.0,#amarelo
		1.0, 1.0, 0.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)   

def inicializaShaders():
    global Shader_programm
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao;
        layout(location = 1) in vec3 vertex_cores;
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = vec4 (vertex_posicao.y, vertex_posicao.x, vertex_posicao.z, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (cores, 1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        glUseProgram(Shader_programm) #ativa o shader

        #desenha o quadrado1
        glBindVertexArray(Vao_quadrado1)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o quadrado2
        glBindVertexArray(Vao_quadrado2)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o quadrado3
        glBindVertexArray(Vao_quadrado3)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o quadrado4
        glBindVertexArray(Vao_quadrado4)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o quadrado5
        glBindVertexArray(Vao_quadrado5)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o quadrado6
        glBindVertexArray(Vao_quadrado6)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        #desenha o triângulo1
        glBindVertexArray(Vao_triangulo1)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        #desenha o triângulo2
        glBindVertexArray(Vao_triangulo2)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        #desenha o triângulo3
        glBindVertexArray(Vao_triangulo3)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.poll_events() #recebe eventos de mouse e teclado

        glfw.swap_buffers(Window) #realiza a troca de buffers para renderizar de fato o que foi desenhado acima
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)): #trata os eventos de mouse e teclado
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaTriangulo1() #modelagem do triângulo1
    inicializaTriangulo2() #modelagem do triângulo2
    inicializaTriangulo3() #modelagem do triângulo3
    inicializaQuadrado1() #modelagem do quadrado1
    inicializaQuadrado2() #modelagem do quadrado2
    inicializaQuadrado3() #modelagem do quadrado3
    inicializaQuadrado4() #modelagem do quadrado4
    inicializaQuadrado5() #modelagem do quadrado5
    inicializaQuadrado6() #modelagem do quadrado5
    inicializaShaders()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()