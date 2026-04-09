import asyncio
import json
import shutil
from pathlib import Path


def setup_nanobot():
    """Lee archivos de tu proyecto y los copia a ~/.nanobot/"""
    
    proyecto_dir = Path(__file__).parent
    nanobot_dir = Path.home() / ".nanobot"
    workspace_dir = nanobot_dir / "workspace"
    
    # Crear directorios
    nanobot_dir.mkdir(exist_ok=True)
    workspace_dir.mkdir(exist_ok=True)
    
    # 1. CONFIG.JSON
    config_src = proyecto_dir / "config.json"
    config_dst = nanobot_dir / "config.json"
    
    if config_src.exists():
        with open(config_src, "r") as f:
            config = json.load(f)
        
        # Actualizar workspace path
        if "agents" in config and "defaults" in config["agents"]:
            config["agents"]["defaults"]["workspace"] = str(workspace_dir)
        
        with open(config_dst, "w") as f:
            json.dump(config, f, indent=2)
        print(f"✅ config.json -> {config_dst}")
    else:
        print(f"❌ No encontré {config_src}")
        return False
    
    # 2. AGENTS.MD
    agents_src = proyecto_dir / "AGENTS.md"
    agents_dst = workspace_dir / "AGENTS.md"
    
    if agents_src.exists():
        shutil.copy(agents_src, agents_dst)
        print(f"✅ AGENTS.md -> {agents_dst}")
    else:
        print(f"⚠️  No encontré {agents_src}")
    
    # 3. TOOLS.MD
    tools_src = proyecto_dir / "TOOLS.md"
    tools_dst = workspace_dir / "TOOLS.md"
    
    if tools_src.exists():
        shutil.copy(tools_src, tools_dst)
        print(f"✅ TOOLS.md -> {tools_dst}")
    else:
        print(f"⚠️  No encontré {tools_src}")
    
    print("\n🎉 Configuración completa!\n")
    return True


async def main():
    from nanobot import Nanobot
    
    if not setup_nanobot():
        print("❌ Error en la configuración")
        return
    
    bot = Nanobot.from_config()
    
    print("=" * 50)
    print("🤖 NANOBOT - Agente del Clima")
    print("=" * 50)
    print("Escribe 'salir' para terminar\n")
    
    while True:
        pregunta = input("👤 Tú: ")
        
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!")
            break
        
        print("\n🔄 Procesando...\n")
        
        result = await bot.run(pregunta, session_key="weather-demo")
        
        print(f"🤖 Nanobot: {result.content}\n")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    asyncio.run(main())