class ResumeCriticAgent:
    def critique(self, bullets: list):
        issues = []

        for bullet in bullets:
            if "worked on" in bullet.lower():
                issues.append("Avoid vague phrases like 'worked on'.")

            if not any(char.isdigit() for char in bullet):
                issues.append("Add measurable impact (numbers/metrics).")

            if "python" not in bullet.lower():
                issues.append("Mention relevant tools/technologies explicitly.")

        return list(set(issues)) 