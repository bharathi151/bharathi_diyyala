{"filter":false,"title":"models.py","tooltip":"/mysite/optimize/models.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":32,"column":39},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":1},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":4},"end":{"row":34,"column":0},"action":"insert","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "],"id":2}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"insert","lines":["#"],"id":3},{"start":{"row":34,"column":1},"end":{"row":34,"column":2},"action":"insert","lines":["p"]},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["r"]},{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"insert","lines":["e"]},{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["f"]}],[{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["e"],"id":4},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["t"]},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["c"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["h"]}],[{"start":{"row":34,"column":9},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":34,"column":1},"end":{"row":34,"column":2},"action":"insert","lines":["s"],"id":8},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["e"]},{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"insert","lines":["l"]},{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["e"]},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["c"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["_"],"id":9},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["r"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["e"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["l"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["a"]},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["t"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["e"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["_"],"id":10},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["r"]},{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["e"]},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["l"]},{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["a"]},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["t"]},{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["e"]},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":[" "],"id":11},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["i"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":[" "],"id":12},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["q"]},{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["u"]},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["e"]},{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"insert","lines":["r"]},{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["y"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["i"],"id":13},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["n"]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["g"]}],[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":14}],[{"start":{"row":37,"column":0},"end":{"row":50,"column":9},"action":"insert","lines":["from django.db import models","","class Topping(models.Model):","    name = models.CharField(max_length=30)","","class Pizza(models.Model):","    name = models.CharField(max_length=50)","    toppings = models.ManyToManyField(Topping)","","    def __str__(self):","        return \"%s (%s)\" % (","            self.name,","            \", \".join(topping.name for topping in self.toppings.all()),","        )"],"id":15}],[{"start":{"row":46,"column":3},"end":{"row":50,"column":9},"action":"remove","lines":[" def __str__(self):","        return \"%s (%s)\" % (","            self.name,","            \", \".join(topping.name for topping in self.toppings.all()),","        )"],"id":16}],[{"start":{"row":46,"column":3},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":47,"column":0},"end":{"row":47,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"remove","lines":[" "],"id":18},{"start":{"row":47,"column":1},"end":{"row":47,"column":2},"action":"remove","lines":[" "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":47,"column":0},"end":{"row":49,"column":97},"action":"insert","lines":["class Restaurant(models.Model):","    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')","    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)"],"id":19}]]},"ace":{"folds":[],"scrolltop":397,"scrollleft":0,"selection":{"start":{"row":49,"column":97},"end":{"row":49,"column":97},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1585740013988,"hash":"631b3f088887445af24d0121291e38f18b5339ed"}