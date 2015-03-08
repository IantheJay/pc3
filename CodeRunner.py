import logging, languageSupport, subprocess

class Evaluate:
    def __init__(self, dataDir):
        self.logger = logging.getLogger("Evaluator")
        self.support = languageSupport.LangSupport(dataDir)

    def evaluate(self, lang, teamFile):
        self.support.compile(lang, teamFile)
        baseName = self.support.generateBaseName(teamFile)
        runTime = self.support.getRunTime(lang)
        return self._run(runTime, baseName)

    def _run(self, runTime, baseName):
        cmd = runTime.replace("{base}", baseName).split()
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return output

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    e = Evaluate("data")
    print e.evaluate("java", "program.java").stdout.read()
