import logging, LanguageSupport, subprocess

class Evaluate:
    def __init__(self, dataDir):
        self.logger = logging.getLogger("Evaluator")
        self.logger.info("Loading an evaluator")
        self.support = LanguageSupport.LangSupport(dataDir)

    def evaluate(self, lang, teamFile, problemDir):
        self.support.compile(lang, teamFile, problemDir)
        baseName = self.support.generateBaseName(teamFile)
        runTime = self.support.getRunTime(lang)
        return self._run(runTime, baseName, problemDir)

    def _run(self, runTime, baseName, problemDir):
        cmd = runTime.replace("{base}", baseName).split()
        self.logger.debug("Attempting to run in " + problemDir)
        self.logger.debug("Attempting to run: " + str(cmd))
        output = subprocess.Popen(cmd, cwd=problemDir, stdout=subprocess.PIPE)
        return self.compare(output.stdout.read(), "Hello World!", True)

    def compare(self, run, good, lazy):
        if lazy:
            good = good.strip()
            run = run.strip()
        runStatus = (run == good)
        self.logger.debug("Expected output: " + good)
        self.logger.debug("Recieved output: " + run)
        self.logger.debug("The run is: " + str(runStatus))
        return runStatus

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    e = Evaluate("data")
    print e.evaluate("java", "program.java").stdout.read()
