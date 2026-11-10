 ## My understanding on Docker  : 

    - Reference video : https://www.bing.com/videos/riverview/relatedvideo?q=Docker+Tutorial+for+Beginners+%e2%80%93+TechWorld+with+Nana.&mid=32A18AE6E8AD371ECA7732A18AE6E8AD371ECA77&churl=&FORM=VIRE
                     :  https://www.youtube.com/watch?v=ZyWBs0CU2wk&t=435s

## What is Docker :

   # 1. What is a container ? 

         - a way to package application with all necessary dependencies and configuration.
         - portable artifact, can be easily shared and moved around.
         - makes development and deployment process more efficient
   
   # 2.  Where do containers live ?

         - Container repository
         - private repository 
         - public repository for docker(hub.docker.com)
   
   # 3. How does container improve development/deployment process ?

         A) Development process : 

            - Before docker :-  (for development applications likes postgres and redis need to be installed on loacl OS with different developers having different versions and many steps so something could go wrong)
            - After Docker :- ( no need to install on local OS it has its own isolated env 
            packages wilth all needed config in one container download on local OS
            diverent versions of 2 app can run on loacl env
            one command to install the app
            )

         B) Deployment process : 

               - Before docker :- (developer -> produce artifacts and instructions to install on server -> operations team -> setup env to deploy application
               
               problems -  install everything on system , textual guide so misunderstanding , dependancy version conflicts. too much back and forth) 

               - After docker :- (Container (config and dependencies) -> prepared by developer and operations team together - > run a docker command pulls the docker image and install on server )

   # 4. What is a container (Technically) ?

      - Layer of images
      - Linux based image , bcoz small in size (alpine:3.10)- base image
      - Aplpication image on top

   # 5. How it works ? 
    
      - Download Docker for desktop
      - Check processor and then download "echo %PROCESSOR_ARCHITECTURE%"
      -Go to hub.docker.com
      - search of postgres offical docker image
      - Run command on terminal "docker run postgres:9.6" (9.6 is the version)
      docker run --name my-postgres -e POSTGRES_PASSWORD=admin123 -p 5432:5432 -d postgres:9.6

   # 6. Docker Image and Docker Container?
      A) Docker Image : 
         - the actual package(config, app, script)
         - artifact, that can be moved around
      B) Docker container : 
         - when u pull image on the local machine creating a container environment

   # 7. Docker vs Virtual Machine (both are virtualization tools) ?

      - OS has two layers 
                  Application (2. layer)
                        |
                  OS kernel (1.Layer)
                        |
                  Hardware (CPU,Memory)
            Kernel communicates with Hardware
      A) Docker  : 
            - virtualizes Application layer ( when u download the docker image on host it virtuliazes application and uses host kernel)
            - Size is smaller than VM
            - Docker containers start and run much fast

      B) VM : 
            - virtualizes both applications aand kernel layer ( when u download the VM image on host it virtuliazes application and  kernel)
            - VM of any OS can run on any OS host

NOTE: Before installing check if virtualization is allowed on ur computer