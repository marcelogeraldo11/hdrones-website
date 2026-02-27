
import os
import re

directory = r'c:\Users\mgera\OneDrive\Documentos\hdrones8\my-project\src\content\blog\es'

# Dictionary of high-confidence replacements for this specific dataset
replacements = {
    r'\bDireccin\b': 'Dirección',
    r'\bAeronutica\b': 'Aeronáutica',
    r'\bAeronutico\b': 'Aeronáutico',
    r'\bAeronuticos\b': 'Aeronáuticos',
    r'\bversin\b': 'versión',
    r'\breas\b': 'áreas',
    r'\brea\b': 'área',
    r'\bms\b': 'más',
    r'\bao\b': 'año',
    r'\baos\b': 'años',
    r'\bdcada\b': 'década',
    r'\btcnica\b': 'técnica',
    r'\btcnicas\b': 'técnicas',
    r'\btcnico\b': 'técnico',
    r'\btcnicos\b': 'técnicos',
    r'\bmximo\b': 'máximo',
    r'\bmxima\b': 'máxima',
    r'\btravs\b': 'través',
    r'\btambin\b': 'también',
    r'\blnea\b': 'línea',
    r'\blneas\b': 'líneas',
    r'\belctrica\b': 'eléctrica',
    r'\belctrico\b': 'eléctrico',
    r'\belctricos\b': 'eléctricos',
    r'\belctricas\b': 'eléctricas',
    r'\bqumica\b': 'química',
    r'\batencin\b': 'atención',
    r'\bdespus\b': 'después',
    r'\bobtencin\b': 'obtención',
    r'\bformacin\b': 'formación',
    r'\bcapacitacin\b': 'capacitación',
    r'\bcertificacin\b': 'certificación',
    r'\bregin\b': 'región',
    r'\bpblico\b': 'público',
    r'\bpblica\b': 'pública',
    r'\bpblicos\b': 'públicos',
    r'\bpblicas\b': 'públicas',
    r'\btecnologa\b': 'tecnología',
    r'\btecnolgica\b': 'tecnológica',
    r'\btecnolgico\b': 'tecnológico',
    r'\btecnolgicos\b': 'tecnológicos',
    r'\btecnolgicas\b': 'tecnológicas',
    r'\bpodrs\b': 'podrás',
    r'\bestarn\b': 'estarán',
    r'\bpodr\b': 'podrá',
    r'\btendrs\b': 'tendrás',
    r'\btendrn\b': 'tendrán',
    r'\bencontrars\b': 'encontrarás',
    r'\bencontrarn\b': 'encontrarán',
    r'\breunin\b': 'reunión',
    r'\bcomisin\b': 'comisión',
    r'\bposicin\b': 'posición',
    r'\bcrtica\b': 'crítica',
    r'\bcrtico\b': 'crítico',
    r'\bcrticos\b': 'críticos',
    r'\bcrticas\b': 'críticas',
    r'\bdinmico\b': 'dinámico',
    r'\bfotogrametra\b': 'fotogrametría',
    r'\bFotogrametra\b': 'Fotogrametría',
    r'\btopografa\b': 'topografía',
    r'\btermografa\b': 'termografía',
    r'\bTermografa\b': 'Termografía',
    r'\bgeografa\b': 'geografía',
    r'\bdrasticamente\b': 'drásticamente',
    r'\bfacil\b': 'fácil',
    r'\bdificil\b': 'difícil',
    r'\bunico\b': 'único',
    r'\bunica\b': 'única',
    r'\bultimo\b': 'último',
    r'\bultima\b': 'última',
    r'\bcodigo\b': 'código',
    r'\bbasico\b': 'básico',
    r'\bnmero\b': 'número',
    r'\banalisis\b': 'análisis',
    r'\banlisis\b': 'análisis',
    r'\bestratgico\b': 'estratégico',
    r'\bestratgica\b': 'estratégica',
    r'\bestratgicos\b': 'estratégicos',
    r'\bestratgicas\b': 'estratégicas',
    r'\blogstica\b': 'logística',
    r'\bminera\b': 'minería',
    r'\bautnomo\b': 'autónomo',
    r'\bautnoma\b': 'autónoma',
    r'\bautnomos\b': 'autónomos',
    r'\bautnomas\b': 'autónomas',
    r'\brabes\b': 'árabes',
    r'\bCanad\b': 'Canadá',
    r'\bprctica\b': 'práctica',
    r'\bprctico\b': 'práctico',
    r'\bprcticos\b': 'prácticos',
    r'\bprcticas\b': 'prácticas',
    r'\bterica\b': 'teórica',
    r'\bterico\b': 'teórico',
    r'\btericos\b': 'teóricos',
    r'\btericas\b': 'teóricas',
    r'\best\b': 'está',
    r'\bestn\b': 'están',
    r'\bestas\b': 'estás',
    r'\bdecisin\b': 'decisión',
    r'\bmnima\b': 'mínima',
    r'\bmnimo\b': 'mínimo',
    r'\bmnimos\b': 'mínimos',
    r'\bmnimas\b': 'mínimas',
    r'\bvehculo\b': 'vehículo',
    r'\bvehculos\b': 'vehículos',
    r'\bartculo\b': 'artículo',
    r'\bquines\b': 'quiénes',
    r'\bquin\b': 'quién',
    r'\bcmo\b': 'cómo',
    r'\bCmo\b': 'Cómo',
    r'\bqu\b': 'qué',
    r'\bQu\b': 'Qué',
    r'\bpor qu\b': 'por qué',
    r'\bPor qu\b': 'Por qué',
    r'\bEsts\b': 'Estás',
    r'\bEst\b': 'Está',
    r'\bproximas\b': 'próximas',
    r'\bproxima\b': 'próxima',
    r'\bproximo\b': 'próximo',
    r'\bproximos\b': 'próximos',
    r'\brpido\b': 'rápido',
    r'\brpida\b': 'rápida',
    r'\brpidamente\b': 'rápidamente',
    r'\bpas\b': 'país',
    r'\bpases\b': 'países',
    r'\benerga\b': 'energía',
    r'\bgestin\b': 'gestión',
    r'\binvestigacin\b': 'investigación',
    r'\bprevencin\b': 'prevención',
    r'\bproteccin\b': 'protección',
    r'\bexpansin\b': 'expansión',
    r'\bregulacin\b': 'regulación',
    r'\bproduccin\b': 'producción',
    r'\binspeccin\b': 'inspección',
    r'\binspecciones\b': 'inspecciones',
    r'\bprxima\b': 'próxima',
    r'\bprximo\b': 'próximo',
    r'\bautonoma\b': 'autonomía',
    r'\ban\b': 'aún',
    r'\ball\b': 'allá',
    r'\bSer\b': 'Será',
    r'\beconmico\b': 'económico',
    r'\beconmica\b': 'económica',
    r'\beconmicos\b': 'económicos',
    r'\beconmicas\b': 'económicas',
    r'\barea\b': 'área',
    r'\bastronutica\b': 'aeronáutica', # Usually drones are aeronautical
}

def fix_content(content):
    # Apply direct replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # 'cin' replacement
    def cin_replacer(match):
        word_start = match.group(1)
        if word_start.lower() in ['fi', 'f']: return match.group(0)
        return word_start + 'ción'
    
    content = re.sub(r'\b([a-zA-ZáéíóúÁÉÍÓÚüÜ]+)cin\b', cin_replacer, content)

    # 'sin' replacement
    def sin_replacer(match):
        word_start = match.group(1)
        if word_start.lower() in ['', 'ver']:
            if word_start.lower() == 'ver': return 'versión'
            return match.group(0)
        return word_start + 'sión'
    
    content = re.sub(r'\b([a-zA-ZáéíóúÁÉÍÓÚüÜ]+)sin\b', sin_replacer, content)
    
    # Fix future tense endings common in these files
    # Note: we only hit these if they are standing alone as words which they seem to do in this broken data
    for verb in ['vivir', 'crecer', 'ser', 'dar', 'har', 'podr', 'tendr', 'habr', 'dir', 'querr', 'sabr', 'valdr', 'saldr', 'vendr']:
        content = re.sub(r'\b' + verb + r'\b', verb + 'á', content)
    
    # Minor fixes
    content = content.replace('seformen', 'se formen')
    content = content.replace('esta creciendo', 'está creciendo')
    content = content.replace('esta listo', 'está listo')
    
    return content

for filename in os.listdir(directory):
    if filename.endswith('.mdx') or filename.endswith('.md'):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_content(content)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Orthography fix v4 complete.")
