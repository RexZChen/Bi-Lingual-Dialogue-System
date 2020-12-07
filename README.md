# Bi-Lingual-Ordering-System
Project check-in's for Georgetown COSC 483

See the menu @ https://www.subway.com/en-US/MenuNutrition/Menu/BreadsAndToppings  

## authors: 
[Zirong Chen](https://github.com/RexZChen); [Haotian Xue](https://github.com/HaotianXue)

## Logs:

* 21/11/2020: **Preliminary structure** decided.
* 22/11/2020: Due to the limitation of our computational resource, we decided to compose our Task-oriented Dialogue System **FROM SCRATCH**.
* 23/11/2020: The **Translator**(v0.1.x are based on Google Translator), **Discriminator** modules completed. DM part(v 0.1.0) partially finished.
* 25/11/2020: New features added for system(v 0.1.1): **Typo handling**, **None-value handling**, **Conclusion function** finished.
* 26/11/2020: New features added for system(v 0.1.2): **New UI**, **“Outliers” handling** finished.
* 27/11/2020: New features added for system(v 0.1.3): **Evaluator**, **Intention correction** finished.
* 28/11/2020: New features added for system(v 0.1.4): **New UI**, **Evalutor debugging** finished.
* 29/11/2020: New features added for system(v 0.1.5): **Evaluator debugging** finished.
* 7/12/2020: New features added for system(v 0.1.6): **Intention Detection debugging** now the intention detector is able to accept multi-words inputs, **Translator Module modified** several more backends included finished.

## Guidance:

* Preparations: ``` Python 3.6.x ```, [translators](https://github.com/UlionTse/translators)
* How to run: ``` python main.py --num_of_turns 10 --task_reward 20 --turn_penalty -1 --score_factor 2 --translator bing ```

## Notice:

* Google Translator might not work due to high volume of current user requests. In order to avoid request failure, now the Translator module supports multiple backends. Currently(v 0.1.6), the module has Google and Bing as its backup backends.
