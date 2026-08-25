# Informática - 2026

## Guía de ejercicios: práctica básica de Git en Windows

**Docente:** Ignacio Lavaggi

> [!IMPORTANT]
> Esta guía tiene como objetivo practicar los comandos básicos de Git desde consola.
>
> Los ejercicios están pensados para realizarse **en orden**, usando **CMD** o **Git Bash** en Windows.
>
> La idea principal es entender tres situaciones diferentes:
>
> 1. Trabajar con Git solamente de forma local.
> 2. Descargar un repositorio que ya existe en un servidor remoto.
> 3. Crear un repositorio local y luego publicarlo en un servidor remoto.

---

## Objetivos de la práctica

Al finalizar esta guía, el estudiante debería poder:

- Instalar y configurar Git.
- Crear y administrar un repositorio local.
- Entender qué son `status`, `add`, `commit` y `log`.
- Clonar un repositorio remoto con `git clone`.
- Identificar la diferencia entre un repositorio local y uno remoto.
- Conectar un repositorio local con uno remoto.
- Utilizar `push` y `pull`.
- Consultar y modificar remotos.
- Trabajar con ramas.
- Utilizar `diff`, `restore` y otros comandos básicos.
- Reconocer errores comunes de Git.

---

## Reglas de trabajo

1. Todos los comandos de Git deben ejecutarse desde consola.
2. Se puede utilizar **CMD** o **Git Bash**.
3. No se debe utilizar GitHub Desktop ni interfaces gráficas para realizar los ejercicios.
4. Cuando sea necesario crear un repositorio remoto, se utilizará el servidor indicado por el docente.
5. Durante toda la práctica conviene ejecutar frecuentemente:

```bash
git status
```

6. Los mensajes de commit deben explicar brevemente qué cambio se realizó.
7. Las preguntas de cada ejercicio deben responderse en la carpeta o archivo indicado por el docente.

---

# Ejercicio 0: instalación y configuración de Git

## Objetivo

Preparar la computadora para poder trabajar con Git desde consola.

> [!IMPORTANT]
> En una computadora personal, esta configuración normalmente se realiza **una sola vez**.
>
> Las computadoras del colegio están **freezadas**, por lo que parte de la configuración puede desaparecer después de reiniciarlas.
>
> Por este motivo, durante las clases hay que acostumbrarse a comprobar rápidamente que Git esté instalado y configurado antes de comenzar.

---

## 0.1 Verificar si Git está instalado

Abrí CMD o Git Bash y ejecutá:

```bash
git --version
```

Si Git está instalado correctamente debería aparecer algo similar a:

```text
git version 2.45.0
```

Si el comando no existe, hay que instalar Git.

Desde PowerShell también se puede instalar con:

```powershell
winget install --id Git.Git -e
```

Después de instalarlo, cerrá y volvé a abrir la consola.

---

## 0.2 Configurar nombre de usuario

Ejecutá:

```bash
git config --global user.name "Tu Nombre"
```

---

## 0.3 Configurar correo

Ejecutá:

```bash
git config --global user.email "tu@email.com"
```

Conviene utilizar el mismo correo con el que te registraste en el servidor remoto.

---

## 0.4 Verificar la configuración

```bash
git config --global user.name
git config --global user.email
```

También se puede consultar toda la configuración:

```bash
git config --list
```

---

## 0.5 Configurar `main` como rama inicial

Para que los repositorios nuevos utilicen `main`:

```bash
git config --global init.defaultBranch main
```

---

## 0.6 Error: `detected dubious ownership`

En las computadoras compartidas del colegio puede aparecer un error parecido a:

```text
fatal: detected dubious ownership in repository at 'C:/...'
```

Git muestra este mensaje cuando considera que la carpeta pertenece a otro usuario de Windows.

Esto puede ocurrir en computadoras compartidas, restauradas o freezadas.

Git normalmente muestra también un comando para solucionar el problema.

La forma recomendada es agregar **solamente el repositorio con el que estamos trabajando** como carpeta segura:

```bash
git config --global --add safe.directory "C:/ruta/del/repositorio"
```

Después volver a probar:

```bash
git status
```

> [!WARNING]
> No conviene marcar indiscriminadamente todas las carpetas de la computadora como seguras.
>
> Agregá solamente la carpeta del repositorio que estés utilizando.

---

## 0.7 Comprobación final

Antes de continuar:

```bash
git --version
git config --global user.name
git config --global user.email
```

### Preguntas

1. ¿Qué versión de Git está instalada?
2. ¿Qué nombre quedó configurado?
3. ¿Qué correo quedó configurado?
4. ¿Para qué sirve configurar nombre y correo?
5. ¿Por qué en las computadoras del colegio puede ser necesario repetir esta configuración?

---

# Ejercicio 1: crear y gestionar un repositorio LOCAL

## Objetivo

Crear un repositorio y trabajar con Git **sin utilizar ningún servidor remoto**.

En este ejercicio todo ocurre dentro de nuestra computadora.

---

## 1.1 Crear una carpeta

Desde CMD o Git Bash:

```bash
mkdir practica-git-local
cd practica-git-local
```

---

## 1.2 Inicializar Git

```bash
git init
```

Verificar:

```bash
git status
```

`git init` convierte la carpeta actual en un repositorio Git.

---

## 1.3 Crear un archivo

Creá un archivo llamado:

```text
README.md
```

Podés hacerlo desde Visual Studio Code o con:

```bash
echo "# Practica Git Local" > README.md
```

Consultar:

```bash
git status
```

---

## 1.4 Agregar el archivo al staging

```bash
git add README.md
```

Volver a consultar:

```bash
git status
```

---

## 1.5 Crear el primer commit

```bash
git commit -m "Crea README inicial"
```

Consultar:

```bash
git status
```

Y luego:

```bash
git log --oneline
```

---

## 1.6 Modificar el archivo

Agregá una nueva línea:

```bash
echo "Este repositorio existe solamente en mi computadora." >> README.md
```

Verificar:

```bash
git status
```

Ver exactamente qué cambió:

```bash
git diff
```

---

## 1.7 Crear un segundo commit

```bash
git add README.md
git commit -m "Agrega descripcion del repositorio"
```

Consultar el historial:

```bash
git log --oneline
```

---

## 1.8 Crear otro archivo

Creá:

```text
notas.txt
```

Por ejemplo:

```bash
echo "Estoy practicando Git." > notas.txt
```

Ahora agregá todos los cambios:

```bash
git add .
```

Y creá otro commit:

```bash
git commit -m "Agrega archivo de notas"
```

---

## Flujo que hay que entender

```text
Modificar archivos
       ↓
git status
       ↓
git add
       ↓
git commit
```

Hasta este momento:

- No usamos Internet.
- No usamos un servidor.
- No usamos `push`.
- No usamos `pull`.
- Git funcionó completamente de forma local.

### Preguntas

1. ¿Qué hace `git init`?
2. ¿Qué diferencia hay entre modificar un archivo y hacer un commit?
3. ¿Para qué sirve `git add`?
4. ¿Qué muestra `git status`?
5. ¿Qué muestra `git log --oneline`?
6. ¿Se necesita Internet para utilizar Git de forma local?

---

# Ejercicio 2: crear un repositorio REMOTO y descargarlo con `git clone`

## Objetivo

Crear un repositorio remoto en GitHub, acceder a la unidad de red del curso y descargar allí una copia local utilizando `git clone`.

---

## 2.1 Abrir la unidad de red del curso

Cada curso tiene asignada una unidad de red en Windows.

Según corresponda, puede ser:

```text
X:
```

o:

```text
W:
```

Primero abrí la unidad de red desde el Explorador de archivos.

Si Windows solicita credenciales, ingresalas normalmente.

Una vez que la unidad esté accesible, abrí CMD o Git Bash.

---

## 2.2 Navegar a la unidad desde consola

Desde CMD:

```bash
X:
```

o:

```bash
W:
```

según la unidad correspondiente al curso.

Verificá el contenido:

```bash
dir
```

Entrá a la carpeta donde vas a trabajar.

---

## 2.3 Crear un repositorio remoto en GitHub

Entrá a GitHub desde el navegador.

Creá un repositorio nuevo.

En este ejercicio, el repositorio debe existir primero en GitHub.

Podés dejar que GitHub cree el repositorio con un archivo inicial, por ejemplo un `README.md`, para que el repositorio remoto no esté vacío.

Copiá la URL HTTPS del repositorio.

---

## 2.4 Clonar el repositorio dentro de la unidad de red

Desde CMD o Git Bash, ubicado dentro de la unidad `X:` o `W:`:

```bash
git clone URL_DEL_REPOSITORIO
```

Esto creará una carpeta nueva dentro de la unidad de red.

---

## 2.5 Entrar al repositorio clonado

```bash
cd NOMBRE_DEL_REPOSITORIO
```

Consultar:

```bash
git status
```

Ver el remoto:

```bash
git remote -v
```

---

## 2.6 Modificar el proyecto

Abrí la carpeta del repositorio con Visual Studio Code.

Realizá una modificación simple en alguno de los archivos.

Después, desde consola:

```bash
git status
```

---

## 2.7 Guardar el cambio localmente

```bash
git add .
git commit -m "Modifica repositorio clonado"
```

Hasta acá, el commit existe en la copia local que está guardada en la unidad de red.

---

## 2.8 Subir el cambio a GitHub

```bash
git push
```

Ahora el commit también queda almacenado en el repositorio remoto de GitHub.

---

## Flujo que hay que entender

```text
Crear repositorio en GitHub
          ↓
Copiar URL
          ↓
Entrar a X: o W:
          ↓
      git clone
          ↓
Modificar archivos
          ↓
      git add .
          ↓
     git commit
          ↓
      git push
          ↓
Actualizar repositorio en GitHub
```

### Preguntas

1. ¿Cuál se creó primero en este ejercicio: el repositorio remoto o la copia local?
2. ¿Qué hace `git clone`?
3. ¿Dónde queda guardada la copia local del repositorio?
4. ¿Qué es `origin`?
5. ¿El `commit` sube automáticamente los cambios a GitHub?
6. ¿Qué hace `git push`?

---

# Ejercicio 3: crear un repositorio LOCAL en la unidad de red y subirlo a GitHub

## Objetivo

Crear un repositorio desde cero dentro de la unidad de red del curso y luego publicarlo en GitHub.

En este ejercicio, el repositorio local debe existir primero.

---

## 3.1 Abrir la unidad de red

Abrí desde Windows la unidad correspondiente al curso:

```text
X:
```

o:

```text
W:
```

Si Windows solicita credenciales, ingresalas.

Después abrí CMD o Git Bash.

---

## 3.2 Navegar a la unidad desde consola

```bash
X:
```

o:

```bash
W:
```

según corresponda.

---

## 3.3 Crear la carpeta del proyecto

```bash
mkdir practica-git-remoto
cd practica-git-remoto
```

---

## 3.4 Inicializar Git

```bash
git init
```

Consultar:

```bash
git status
```

---

## 3.5 Crear archivos

Creá:

```text
README.md
```

y:

```text
programa.py
```

Los archivos pueden crearse desde Visual Studio Code.

---

## 3.6 Crear el primer commit

```bash
git status
git add .
git commit -m "Crea proyecto inicial"
```

Consultar:

```bash
git log --oneline
```

Hasta este punto, el repositorio existe solamente en la unidad de red.

---

## 3.7 Crear un repositorio vacío en GitHub

Entrá a GitHub desde el navegador.

Creá un repositorio nuevo.

> [!IMPORTANT]
> En este ejercicio el repositorio remoto debe crearse **vacío**.
>
> No agregar README, `.gitignore` ni licencia desde GitHub, porque el contenido ya existe en el repositorio local.

Copiá la URL HTTPS del repositorio.

---

## 3.8 Conectar el repositorio local con GitHub

Desde la consola, dentro de la carpeta del proyecto:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Verificar:

```bash
git remote -v
```

---

## 3.9 Asegurar que la rama principal sea `main`

```bash
git branch -M main
```

---

## 3.10 Realizar el primer push

```bash
git push -u origin main
```

La opción `-u` vincula la rama local `main` con la rama remota correspondiente.

Después de esta primera vez, normalmente alcanza con:

```bash
git push
```

---

## 3.11 Hacer un nuevo cambio

Modificá alguno de los archivos del proyecto.

Después:

```bash
git status
git add .
git commit -m "Agrega nuevo cambio"
git push
```

---

## Flujo que hay que entender

```text
Entrar a X: o W:
       ↓
Crear carpeta
       ↓
    git init
       ↓
Crear archivos
       ↓
    git add .
       ↓
   git commit
       ↓
Crear repositorio vacío en GitHub
       ↓
git remote add origin URL
       ↓
git push -u origin main
```

### Preguntas

1. ¿Cuál se creó primero en este ejercicio: el repositorio local o el remoto?
2. ¿Dónde está físicamente guardado el repositorio local?
3. ¿Qué hace `git remote add origin URL`?
4. ¿Para qué sirve `git remote -v`?
5. ¿Qué hace `git push -u origin main`?
6. ¿Por qué el repositorio remoto debe crearse vacío?
7. ¿Cuál es la diferencia principal entre el ejercicio 2 y el ejercicio 3?

---

# Ejercicio 4: practicar `pull` y `push`

## Objetivo

Entender cómo se sincronizan los cambios entre una copia local y el repositorio remoto.

## Consigna

Utilizá el repositorio del ejercicio 3.

Desde la página del servidor, realizá un pequeño cambio en un archivo del repositorio.

Después, en la copia local:

```bash
git pull
```

Verificá que el cambio aparezca.

Luego realizá otro cambio local:

```bash
git status
git add .
git commit -m "Agrega cambio local"
git push
```

### Preguntas

1. ¿Qué hace `git push`?
2. ¿Qué hace `git pull`?
3. ¿Qué pasa si hacemos un commit pero nunca ejecutamos `git push`?
4. ¿Por qué conviene hacer `git pull` antes de comenzar a trabajar en un proyecto compartido?

---

# Ejercicio 5: ver diferencias e historial

## Objetivo

Utilizar Git para investigar qué cambios existen y qué cambios se realizaron anteriormente.

Modificar un archivo sin hacer commit.

Después ejecutar:

```bash
git status
```

Luego:

```bash
git diff
```

Agregar el archivo:

```bash
git add .
```

Ahora ejecutar:

```bash
git diff --staged
```

Crear el commit:

```bash
git commit -m "Practica diff"
```

Consultar:

```bash
git log
```

y:

```bash
git log --oneline
```

### Preguntas

1. ¿Qué muestra `git diff`?
2. ¿Qué muestra `git diff --staged`?
3. ¿Qué diferencia hay entre `git log` y `git log --oneline`?
4. ¿Para qué sirve consultar el historial?

---

# Ejercicio 6: trabajar con branches o ramas

## Objetivo

Crear una rama para trabajar sin modificar directamente `main`.

Una **branch** o rama es una línea de trabajo separada dentro del mismo repositorio.

Ver ramas:

```bash
git branch
```

Crear una rama y entrar en ella:

```bash
git switch -c feature/presentacion
```

Modificar `README.md`.

Después:

```bash
git add README.md
git commit -m "Agrega presentacion desde rama"
```

Consultar:

```bash
git log --oneline --graph --all
```

Volver a `main`:

```bash
git switch main
```

### Preguntas

1. ¿El cambio realizado en la rama aparece automáticamente en `main`?
2. ¿Para qué puede servir trabajar en una rama diferente?
3. ¿Qué muestra `git log --oneline --graph --all`?

---

# Ejercicio 7: unir una rama con `merge`

## Objetivo

Integrar los cambios de otra rama dentro de `main`.

Primero asegurate de estar en `main`:

```bash
git switch main
```

Luego:

```bash
git merge feature/presentacion
```

Consultar:

```bash
git status
git log --oneline --graph --all
```

Subir:

```bash
git push
```

### Preguntas

1. ¿Qué hace `git merge`?
2. ¿Por qué importa en qué rama estamos ubicados antes del merge?
3. ¿Qué cambió en `main` después de realizarlo?

---

# Ejercicio 8: comparar `fetch` y `pull`

## Objetivo

Entender la diferencia entre descargar información del remoto y aplicar sus cambios.

Ejecutar:

```bash
git fetch
```

Consultar:

```bash
git log --oneline --all --graph
```

Luego:

```bash
git pull
```

### Preguntas

1. ¿Qué hace `git fetch`?
2. ¿Qué hace `git pull`?
3. ¿Cuál modifica directamente nuestros archivos?
4. ¿Para qué puede ser útil ejecutar `fetch`?

---

# Ejercicio 9: deshacer cambios antes de un commit

## Objetivo

Descartar un cambio local todavía no registrado.

Modificar `README.md`.

Consultar:

```bash
git status
git diff
```

Después:

```bash
git restore README.md
```

Consultar nuevamente:

```bash
git status
```

### Preguntas

1. ¿Qué hizo `git restore`?
2. ¿El cambio descartado fue incluido en algún commit?
3. ¿Por qué hay que tener cuidado al utilizar este comando?

---

# Ejercicio 10: sacar archivos del staging

## Objetivo

Comprender la diferencia entre un archivo modificado y un archivo preparado para commit.

Modificar un archivo.

Agregarlo:

```bash
git add archivo.txt
```

Consultar:

```bash
git status
```

Sacarlo del staging:

```bash
git restore --staged archivo.txt
```

Consultar nuevamente:

```bash
git status
```

### Preguntas

1. ¿Se borraron las modificaciones del archivo?
2. ¿Qué cambió después de `git restore --staged`?
3. ¿Qué es el staging?

---

# Ejercicio 11: cambiar la dirección de un remoto

## Objetivo

Reconocer y resolver el error `remote origin already exists`.

Ver el remoto:

```bash
git remote -v
```

Intentar agregar otro `origin`:

```bash
git remote add origin URL
```

Debería aparecer:

```text
remote origin already exists
```

Para modificar la URL existente:

```bash
git remote set-url origin URL_NUEVA
```

Consultar:

```bash
git remote -v
```

### Preguntas

1. ¿Por qué aparece `remote origin already exists`?
2. ¿Qué diferencia hay entre `remote add` y `remote set-url`?
3. ¿Cómo verificamos la URL actual del remoto?

---

# Ejercicio 12: mini proyecto final

## Objetivo

Integrar los conceptos principales de la guía.

Crear un repositorio llamado:

```text
mini-proyecto-git
```

Debe contener:

```text
README.md
src/
    app.py
notas.txt
```

El `README.md` debe incluir:

```text
Nombre del proyecto
Descripción
Comandos de Git utilizados
```

`src/app.py` debe contener un programa Python sencillo.

`notas.txt` debe incluir al menos tres notas sobre lo aprendido.

## Requisitos

El proyecto debe tener:

- Un repositorio local.
- Un repositorio remoto en el servidor indicado por el docente.
- Al menos tres commits con mensajes claros.
- Una rama llamada `feature/mejora-readme`.
- Un merge de esa rama hacia `main`.
- Un push final al remoto.

## Entrega

Entregar:

1. URL del repositorio remoto.
2. Captura o salida de:

```bash
git log --oneline --graph --all
```

3. Captura o salida de:

```bash
git status
```

sin cambios pendientes.

4. Responder:

- ¿Qué es un repositorio local?
- ¿Qué es un repositorio remoto?
- ¿Qué es un commit?
- ¿Qué hace `git clone`?
- ¿Qué diferencia hay entre `push` y `pull`?
- ¿Qué es una branch?
- ¿Para qué sirve `git status`?

---

# Cheatsheet de comandos Git

## Configuración

| Acción | Comando |
|---|---|
| Ver versión instalada | `git --version` |
| Configurar nombre | `git config --global user.name "Nombre"` |
| Configurar correo | `git config --global user.email "correo"` |
| Ver configuración | `git config --list` |
| Usar `main` por defecto | `git config --global init.defaultBranch main` |
| Agregar repo como carpeta segura | `git config --global --add safe.directory "RUTA"` |

---

## Trabajo local

| Acción | Comando |
|---|---|
| Crear repositorio | `git init` |
| Ver estado | `git status` |
| Agregar un archivo | `git add archivo` |
| Agregar todos los cambios | `git add .` |
| Crear commit | `git commit -m "mensaje"` |
| Ver historial | `git log` |
| Ver historial corto | `git log --oneline` |
| Ver cambios | `git diff` |
| Ver cambios preparados | `git diff --staged` |

---

## Repositorios remotos

| Acción | Comando |
|---|---|
| Clonar repositorio | `git clone URL` |
| Ver remotos | `git remote -v` |
| Agregar remoto | `git remote add origin URL` |
| Cambiar URL del remoto | `git remote set-url origin URL` |
| Primer push | `git push -u origin main` |
| Subir commits | `git push` |
| Traer y aplicar cambios | `git pull` |
| Traer información sin aplicarla | `git fetch` |

---

## Ramas

| Acción | Comando |
|---|---|
| Ver ramas | `git branch` |
| Crear rama y entrar | `git switch -c nombre-rama` |
| Cambiar de rama | `git switch nombre-rama` |
| Renombrar rama actual a `main` | `git branch -M main` |
| Fusionar una rama | `git merge nombre-rama` |

---

## Deshacer cambios

| Acción | Comando |
|---|---|
| Restaurar archivo | `git restore archivo` |
| Sacar archivo del staging | `git restore --staged archivo` |

---

## Flujo básico local

```bash
git status
git add .
git commit -m "mensaje"
```

---

## Flujo de un repositorio ya clonado

```bash
git pull
git status
git add .
git commit -m "mensaje"
git push
```

---

## Crear local y publicar en remoto

```bash
git init
git add .
git commit -m "Primer commit"
git remote add origin URL
git branch -M main
git push -u origin main
```

---

## Clonar un repositorio existente

```bash
git clone URL
cd repositorio
git status
```

---

## Idea principal

```text
git commit = guarda cambios LOCALMENTE

git push   = envía commits al REMOTO

git pull   = trae cambios desde el REMOTO

git clone  = crea una copia LOCAL de un repositorio REMOTO
```
