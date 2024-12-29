import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

class AnalisiStatistica:
    def __init__(self, dati: pd.DataFrame):
        """
        Inizializza l'analizzatore statistico con un DataFrame.
        
        Args:
            dati (pd.DataFrame): DataFrame con 4 variabili
        """
        self.dati = dati
        self.risultati = {}

    def calcola_statistiche(self) -> Dict:
        """
        Calcola media, mediana e moda per ogni variabile.
        
        Returns:
            Dict: Dizionario con i risultati statistici
        """
        for colonna in self.dati.columns:
            self.risultati[colonna] = {
                'media': np.mean(self.dati[colonna]),
                'mediana': np.median(self.dati[colonna]),
                'moda': stats.mode(self.dati[colonna])[0][0]
            }
        return self.risultati

    def genera_report(self) -> str:
        """
        Genera un report testuale delle statistiche.
        
        Returns:
            str: Report formattato
        """
        report = "REPORT ANALISI STATISTICA\n" + "="*50 + "\n\n"
        
        for variabile, stats in self.risultati.items():
            report += f"Variabile: {variabile}\n"
            report += f"  Media:   {stats['media']:.2f}\n"
            report += f"  Mediana: {stats['mediana']:.2f}\n"
            report += f"  Moda:    {stats['moda']:.2f}\n"
            report += "-"*50 + "\n"
        
        return report

    def visualizza_distribuzioni(self):
        """
        Crea un grafico con gli istogrammi delle distribuzioni.
        """
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes = axes.ravel()
        
        for idx, colonna in enumerate(self.dati.columns):
            axes[idx].hist(self.dati[colonna], bins=20, edgecolor='black')
            axes[idx].set_title(f'Distribuzione di {colonna}')
            axes[idx].axvline(self.risultati[colonna]['media'], 
                            color='red', linestyle='--', label='Media')
            axes[idx].axvline(self.risultati[colonna]['mediana'], 
                            color='green', linestyle='--', label='Mediana')
            axes[idx].axvline(self.risultati[colonna]['moda'], 
                            color='blue', linestyle='--', label='Moda')
            axes[idx].legend()
        
        plt.tight_layout()
        return fig

# Esempio di utilizzo
def main():
    # Creiamo dei dati di esempio
    np.random.seed(42)
    dati_esempio = pd.DataFrame({
        'Variabile1': np.random.normal(100, 15, 1000),
        'Variabile2': np.random.exponential(50, 1000),
        'Variabile3': np.random.uniform(0, 100, 1000),
        'Variabile4': np.random.gamma(2, 2, 1000)
    })
    
    # Inizializziamo l'analizzatore
    analizzatore = AnalisiStatistica(dati_esempio)
    
    # Calcoliamo le statistiche
    analizzatore.calcola_statistiche()
    
    # Generiamo e stampiamo il report
    print(analizzatore.genera_report())
    
    # Visualizziamo le distribuzioni
    analizzatore.visualizza_distribuzioni()
    plt.show()

if __name__ == "__main__":
    main()
