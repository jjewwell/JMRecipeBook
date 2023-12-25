
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
#imports

class RecipeBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jewell's Favorite Cookie Recipes")
        self.root.minsize(500,475)

        self.recipe_book = RecipeBook()

        self.recipe_listbox = tk.Listbox(root, width=500, height=475, activestyle=tk.NONE, highlightcolor="orchid4",
                                         highlightbackground="orchid4", justify="center",
                                         font=Font(family="Times", size=13))
        self.recipe_listbox.configure(background="plum2", foreground="orchid4")
        self.recipe_listbox.configure(selectbackground="plum2")
        self.recipe_listbox.pack(padx=0, pady=0, side = LEFT, expand = TRUE, fill = BOTH)
        #Sets color, dimensions, font, alignment, and highlight color of listbox

        self.cc_button = tk.Button(root, text="Chocolate Chip Cookies", command=self.list_CC_instructions)
        self.cc_button.configure(background="orchid4", foreground = "plum2")
        self.cc_button.place(relx=.03, rely=.1715)
        self.sd_button = tk.Button(root, text="Snickerdoodles", command=self.list_SD_instructions)
        self.sd_button.configure(background="orchid4", foreground="plum2")
        self.sd_button.place(relx=.2, rely=.1715)
        self.rv_button = tk.Button(root, text="Red Velvet Cookies", command=self.list_RV_instructions)
        self.rv_button.configure(background="orchid4", foreground="plum2")
        self.rv_button.place(relx=.035, rely=.46)
        self.sb_button = tk.Button(root, text="Shortbread Cookies", command=self.list_SB_instructions)
        self.sb_button.configure(background="orchid4", foreground="plum2")
        self.sb_button.place(relx=.695, rely=.46)
        self.scb_button = tk.Button(root, text="Sugar Cookie Bars", command=self.list_SCB_instructions)
        self.scb_button.configure(background="orchid4", foreground="plum2")
        self.scb_button.place(relx=.86, rely=.46)
        self.pbc_button = tk.Button(root, text="Peanut Butter Cup Cookies", command=self.list_PBC_instructions)
        self.pbc_button.configure(background="orchid4", foreground="plum2")
        self.pbc_button.place(relx=.68, rely=.1715)
        self.ccc_button = tk.Button(root, text="Chocolate Crinkle Cookies", command=self.list_CCC_instructions)
        self.ccc_button.configure(background="orchid4", foreground="plum2")
        self.ccc_button.place(relx=.84, rely=.1715)
        self.poc_button = tk.Button(root, text="Pumpkin Oatmeal Cookies", command=self.list_POC_instructions)
        self.poc_button.configure(background="orchid4", foreground="plum2")
        self.poc_button.place(relx=.18, rely=.46)
        self.cacc_button = tk.Button(root, text="Cookies and Cream Cookies", command=self.list_CandCC_instructions)
        self.cacc_button.configure(background="orchid4", foreground="plum2")
        self.cacc_button.place(relx=.09, rely=.75)
        self.pmc_button = tk.Button(root, text="Peppermint Mocha Cookies", command=self.list_PMC_instructions)
        self.pmc_button.configure(background="orchid4", foreground="plum2")
        self.pmc_button.place(relx=.75, rely=.75)
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.configure(background="firebrick2", foreground="wheat1", height= 1, width =10 )
        self.exit_button.place(relx=.455, rely = .85)

        for i in range(8):
            self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "Welcome to Jewell's Favorite Cookie Recipes!")
        self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "My name is Jewell, and I'm a self-taught baker.")
        self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "One of my favorite things in the entire WORLD is a warm batch of cookies.")
        self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "So, I have gathered 10 of my favorite cookie recipes for you to enjoy!")
        for i in range(4):
            self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "Most of these recipes are adapted from Sally McKenney's blog, Sally's Baking Addiction.")
        self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "Without further ado, click the name of any recipe to view it.")
        self.recipe_listbox.insert(tk.END, "")
        self.recipe_listbox.insert(tk.END, "Happy baking! ""\u2764\uFE0F""")

    def move_buttons(self):
        self.recipe_listbox.config(justify="left")
        self.cc_button.place(relx=.41, rely=.1715)
        self.sd_button.place(relx=.56, rely=.1715)
        self.rv_button.place(relx=.42, rely=.33)
        self.poc_button.place(relx=.54, rely=.33)
        self.sb_button.place(relx=.695, rely=.33)
        self.scb_button.place(relx=.86, rely=.33)
        self.pmc_button.place(relx=.75, rely=.25)
        self.cacc_button.place(relx=.47, rely=.25)
    def list_CC_instructions(self):
        self.move_buttons()
        CC_instructions = self.recipe_book.recipes[self.recipe_book.getChocolateChips()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Chocolate Chip Cookies: Yields 24 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in CC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in CC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_SD_instructions(self):
        self.move_buttons()
        SD_instructions = self.recipe_book.recipes[self.recipe_book.getSnickerdoodles()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Snickerdoodles: Yields 36 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in SD_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in SD_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)
    def list_RV_instructions(self):
        self.move_buttons()
        RV_instructions = self.recipe_book.recipes[self.recipe_book.getRedVelvet()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Red Velvet Cookies: Yields 20 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in RV_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in RV_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_SB_instructions(self):
        self.move_buttons()
        SB_instructions = self.recipe_book.recipes[self.recipe_book.getShortbread()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Shortbread Cookies: Yield depends on the size of the cookie cutter,"
                                           " about 50 cookies with a 2 inch circle cutter")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in SB_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in SB_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_SCB_instructions(self):
        self.move_buttons()
        SCB_instructions = self.recipe_book.recipes[self.recipe_book.getCookieBars()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Sugar Cookie Bars: 20-24 bars")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in SCB_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in SCB_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_PBC_instructions(self):
        self.move_buttons()
        PBC_instructions = self.recipe_book.recipes[self.recipe_book.getPBCookies()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Peanut Butter Cup Cookies: Yields 24 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in PBC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in PBC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_CCC_instructions(self):
        self.move_buttons()
        CCC_instructions = self.recipe_book.recipes[self.recipe_book.getCrinkleCookies()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Chocolate Crinkle Cookies: Yields 20 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in CCC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in CCC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_POC_instructions(self):
        self.move_buttons()
        POC_instructions = self.recipe_book.recipes[self.recipe_book.getPumpkinOatCookies()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Pumpkin Oatmeal Cookies: Yields 30 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in POC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in POC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_CandCC_instructions(self):
        self.move_buttons()
        CandCC_instructions = self.recipe_book.recipes[self.recipe_book.getCookiesAndCream()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Cookies and Cream Cookies: Yields 30 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in CandCC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in CandCC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)

    def list_PMC_instructions(self):
        self.move_buttons()
        PMC_instructions = self.recipe_book.recipes[self.recipe_book.getPeppermintMochaCookies()]
        self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
        self.recipe_listbox.insert(tk.END, "Peppermint Mocha Cookies: Yields 20 cookies")
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Ingredients:")
        self.recipe_listbox.insert(tk.END, "\n")
        for ingredients_name in PMC_instructions['ingredients']:
            self.recipe_listbox.insert(tk.END, ingredients_name)
        self.recipe_listbox.insert(tk.END, "\n")
        self.recipe_listbox.insert(tk.END, "Instructions:")
        self.recipe_listbox.insert(tk.END, "\n")
        for instructions_name in PMC_instructions['instructions']:
            self.recipe_listbox.insert(tk.END, instructions_name)
    #all of the above functions print the instructions and ingredients of each recipe
class RecipeBook:
    def __init__(self):
        self.recipes = {
            'Chocolate Chip Cookies': {
                'ingredients': ['- 2 and 1/4 cups of all-purpose flour', '- 3/4 cup of salted butter', '- 1 egg and 1 egg yolk',
                                '- 3/4 cup of brown sugar', '- 1/2 cup granulated sugar', '- 2 teaspoons vanilla extract',
                                '- 1 teaspoon baking soda', '- 1 and 1/4 cup chocolate chips', '- 1 teaspoon cornstarch',
                                '- optional: 1 teaspoon ground cinnamon'],
                'instructions': ['1. Melt the butter in the microwave. Allow it to cool on the counter for 2 minutes. \n',
                                '2. With a whisk or stand mixer with a whisk attatchment,'
                                ' mix melted butter, granulated sugar, and brown sugar until thick in a large mixing bowl.\n',
                                '3. Mix in the vanilla extract, egg, and egg yolk until combined.\n',
                                '4. With a spatula, stir in the all-purpose flour, baking soda, cornstarch, and ground cinnamon (optional). \n',
                                '5. Stir in the chocolate chips. Dough should be thick and wet. \n',
                                '6. Allow dough to chill in the fridge for 1 hour.\n',
                                '7. Roll dough into 1.5 tablespoon balls and preheat the oven to 325 degrees fahrenheit. \n',
                                '8. Put onto baking sheet and bake for 11-13 minutes, until edges are golden-brown. '
                                'Allow cookies to cool on the baking sheet for 5 minutes before moving to a wire rack.']
            },
            'Snickerdoodles': {
                'ingredients': ['- 3 cups of all-purpose flour', '- 2 teaspoons cream of tartar', '- 1 teaspoon baking soda',
                                '- 1 cup salted and softened butter',
                                '- 1 and 1/2 teaspoons ground cinnamon, plus another 2 teaspoons for topping',
                                '- 1 and 1/3 cup granulated sugar, plus another 1/3 cup for topping', '- 1 egg and 1 egg yolk',
                                '- 2 teaspoons vanilla extract'],
                'instructions': ['1. Preheat the oven to 375 degrees fahrenheit.'
                                 ' Mix the granulated sugar and cinnamon in a small bowl for the topping. \n',
                                 '2. Whisk the all-purpose flour, cream of tartar, baking soda, and ground cinnamon in a medium bowl. \n',
                                 '3. In a large bowl, beat the softened butter and remaining granulated sugar until '
                                 'smooth with a hand mixer fitted with a spatula attachment.',
                                 '4. Add the egg, an egg yolk, and vanilla extract to the large bowl. Mix until combined.\n',
                                 '5. Add the dry ingredients to the wet ingredients slowly. The dough should be thick. \n',
                                 '6. Roll cookie dough into 1.5 tablespoon balls. Roll the balls into the previously prepared topping.'
                                 ' Put onto baking sheet and bake for 10 minutes until puffy and soft.']
            },
            'Red Velvet Cookies': {
                'ingredients': ['- 1 and 2/3 cup all-purpose flour', '- 1/4 cup cocoa powder', '- 1 teaspoon baking soda',
                                '- 1/2 cup of softened and salted butter', '- 3/4 cup brown sugar', '- 1/4 cup granulated sugar',
                                '- 1 egg', '- 1 tablespoon milk', '- 2 teaspoons vanilla extract', '- 3/4 teaspoon red gel food coloring',
                                '- 1 and 1/4 cup white chocolate chips'],
                'instructions': ['1. Using a stand mixer with a spatula attachment,'
                                 ' beat the salted butter, brown sugar, and granulated sugar until creamy.\n ',
                                 '2. Add in the egg and teaspoons of vanilla extract. Mix until combined.\n',
                                 '3. Pour the all purpose flour, cocoa powder, and baking soda into the bowl of wet ingredients.'
                                 ' Mix until combined.\n',
                                 '4. Add the milk and red gel food coloring. Mix until sticky. Then, add in white chocolate chips.\n',
                                 '5. Allow dough to chill in the fridge for an hour. \n',
                                 '6. Preheat oven to 350 degrees fahrenheit. Scoop cookie dough into 1.5 tablespoon balls.'
                                 ' Put onto baking sheet and bake for 11-13 minutes or until edges are set.']
            },
            'Shortbread Cookies': {
                'ingredients': ['- 1 and 1/2 cup salted and softened butter', '- 2 and 3/4 cups all-purpose flour',
                                '- 1 cup powdered sugar', '- 1 teaspoon vanilla extract', '- 1 to 2 teaspoons water'],
                'instructions' : ['1. Preheat oven to 350 degrees fahrenheit.\n',
                                  '2. Beat the butter with a stand mixer fitted with a spatula attachment until creamy.\n',
                                  '3. Add the powdered sugar and vanilla extract and mix until smooth.\n',
                                  '4. Switch the mixer to low speed and add the all purpose flour in 1/4 cup incrememnts.'
                                  ' Once incorporated, beat until the dough becomes smooth. \n',
                                  '5. Add in 1 to 2 teaspoons of water if the dough is still not combined. \n',
                                  '6. Lightly flour a work surface. Using a rolling pin, roll out the dough into a 1/4 inch slab. '
                                  'Cut into shapes with a cookie cutter.\n',
                                  '7. Place onto the baking sheet and cook for 12 to 14 minutes, or until lightly browned on edges.']
            },
            'Sugar Cookie Bars' : {
                'ingredients' : ['- 1 and 1/2 cup of salted and softened butter', '- 2 and 1/2 cups powdered sugar',
                                 '- 2 tablespoons heavy cream', '- 1/4 teaspoon salt', '- 3 teaspoons vanilla extract',
                                 '- 2 and 3/4 cups all-purpose flour', '- 1 and 1/2 teaspoon baking powder', '- 1 and 1/4 cup granulated sugar',
                                 '- 1 egg and an egg yolk'],
                'instructions' : ['1. Preheat oven to 350 degrees fahrenheit. Spray a 9x13 baking dish with nonstick spray.\n',
                                  '2. Using a handheld mixer fitted with a spatula attachment,'
                                  ' beat 2 sticks of butter and the granulated sugar on medium speed until creamed. \n',
                                  '3. Add an egg, an egg yolk, and the vanilla extract to the mixture and beat on high speed until combined.\n',
                                  '4. Add the all-purpose flour, baking powder, and a pinch of salt to the wet ingredients and '
                                  'mix on low until combined. \n',
                                  '5. Press the dough into the prepared baking dish and cook for 20-22 minutes.'
                                  ' Let the bars cool in the pan for 30 minutes.\n',
                                  '6. For the frosting: Add a stick of butter, the powdered sugar, heavy cream, and vanilla extract to a bowl. '
                                  'Mix using a stand mixer with a paddle attachment.\n',
                                  '7. After the bars have cooled, cut them into squares and decorate with the buttercream frosting.']

            },
            'Peanut Butter Cup Cookies' : {
                'ingredients' : ['- 1 and 1/4 cup all-purpose flour', '- 1/2 teaspoon baking soda', '- 1/2 cup butter',
                                 '- 1/2 cup brown sugar', '- 1/4 cup granulated sugar', '- 3/4 cup creamy peanut butter',
                                 '- 1 egg', '- 1 teaspoon vanilla extract', '- 24 unwrapped Reese mini cups'],
                'instructions' : ['1. Cream the butter, brown sugar, and granulated sugar with a stand mixer fitted with a paddle attachment.\n',
                                  '2. Once combined, beat in the creamy peanut butter, 1 egg, and vanilla extract on high speed until light in color.\n',
                                  '3. With the speed on low, slowly pour in the all-purpose flour and baking soda. Mix until combined.\n',
                                  '4. Cover tightly and chill the dough for one hour in the refrigerator.\n',
                                  '5. Preheat the oven to 350 degrees fahrenheit. '
                                  'Pour 1/2 cup granulated sugar into a small bowl for the topping.\n',
                                  '6. Roll cookies in 1.5 tablespoon balls. Roll each ball in the granulated sugar topping.'
                                  ' Put on baking sheet and bake for 11-13 minutes.\n',
                                  '7. Allow cookies to cool on the baking sheet for 5 minutes. '
                                  'Then, press 1 peanut butter cup into the center of each cookie.\n',
                                  '8. Move the cookies onto a freezer-safe dish and freeze for 10-15 minutes, '
                                  'or until the peanut butter cup has set.\n']

            },
            'Chocolate Crinkle Cookies' : {
                'ingredients' : ['- 1 and 1/2 cup all-purpose flour', '- 1 cup granulated sugar', '- 1/2 cup brown sugar',
                                 '- 1 and 1/2 teaspoon baking powder', '- 6 tablespoons of melted and salted butter',
                                 '- 3/4 cup cocoa powder', '- 3 eggs', '- 1 teaspoon vanilla extract', '- 1/2 cup powdered sugar'],
                'instructions' : ['1. Preheat oven to 350 degrees fahrenheit.\n',
                                  '2. Whisk the all-purpose flour, granulated sugar, brown sugar, and baking powder in a large bowl.\n',
                                  '3. Melt the butter in the microwave. Then, add the cocoa powder and combine until thick and paste-like.\n',
                                  '4. Stir in the eggs and vanilla extract.\n',
                                  '5. Pour the wet ingredients into the dry ingredients and combine using a spatula.\n',
                                  '6. Roll into 1 tablespoon balls of dough. Then, roll each ball in powdered sugar to coat. '
                                  'Put on baking sheet and bake for 12-13 minutes until cracks appear. \n',
                                  '7. Top with more powdered sugar if needed and let them cool on the baking sheet for 5 minutes.']
            },
            'Pumpkin Oatmeal Cookies' : {
                'ingredients' : ['- 2 cups and 1 tablespoon all-purpose flour', '- 1 teaspoon baking soda', '- 2 teaspoons ground cinnamon',
                                 '- 2 teaspoons pumpkin pie spice', '- 1 and 1/2 cup whole rolled oats',
                                 '- 2 sticks of salted and melted butter', '- 3 tablespoons maple syrup', '- 3/4 cup brown sugar',
                                 '- 1/2 cup granulated sugar', '- 1 egg yolk', '- 3/4 cup pumpkin puree',
                                 '- 2 teaspoons vanilla extract', '- 1 and 1/2 cup chocolate chips'],
                'instructions' : ['1. Preheat the oven to 350 degrees fahrenheit.\n',
                                  '2. Melt the butter in the microwave. While it cools, blot the pumpkin puree with a paper towel to'
                                  ' prevent excess moisture.\n',
                                  '3. Whisk the melted butter, maple syrup, brown sugar, granulated sugar, egg yolk, the blotted pumpkin puree,'
                                  ' and vanilla extract together.\n',
                                  '4. Mix in the all-purpose flour, baking soda, ground cinnamon, and pumpkin pie spice.'
                                  ' Then, fold in the oats and chocolate chips with a spatula.\n',
                                  '5. Scoop dough into 1.5 tablespoon balls. Flatten slightly, put on baking sheet, '
                                  'and bake for 13-14 minutes until sides are slightly browned.\n',
                                  '6. Remove from the oven and allow cookies to cool on the baking sheet for 5 minutes.']

            },
            'Cookies and Cream Cookies' : {
                'ingredients' : ['- 2 and 1/4 cups all-purpose flour', '- 1 and 1/2 teaspoon cornstarch', '- 1 teaspoon baking soda',
                                 '- 1/2 cup granulated sugar', '- 3/4 cup softened and salted butter',
                                 '- 4 ounces of softened and full-fat brick cream cheese', '- 1/2 cup brown sugar',
                                 '- 1 egg', '- 2 teaspoons vanilla extract', '- 1 cup white chocolate chips',
                                 '- 1 and 1/4 cup chopped oreos'],
                'instructions' : ['1. In a large bowl using a stand mixer fitted with a paddle attachment, '
                                  'beat the brick cream cheese and butter on high speed until combined.\n',
                                  '2. Add in the brown sugar and granulated sugar, and mix until creamed.'
                                  ' Then, add the egg and vanilla extract, and mix until combined.\n',
                                  '3. Add the all-purpose flour, cornstarch, and baking soda. Mix until dough is heavy and combined.\n',
                                  '4. Add in the white chocolate chips and chopped oreos.\n',
                                  '5. Cover and chill the dough for 2 hours in the refrigerator. Preheat the oven to 350 degrees fahrenheit.',
                                  '6. Roll cookie dough into balls - 1.5 tablespoons of dough per cookie.'
                                  ' Put onto baking sheet and bake for 12-13 minutes or until lightly browned on the sides.\n',
                                  '7. Remove from the oven and allow cookies to cool on the baking sheet for 5 minutes.']

            },
            'Peppermint Mocha Cookies' : {
                'ingredients' : ['- 1/2 cup of softened and salted butter', '- 1/2 cup granulated sugar',
                                 '- 1/2 cup brown sugar', '- 1 egg', '- 1 teaspoon vanilla extract',
                                 '- 1 teaspoon peppermint extract', '- 1 cup of all-purpose flour',
                                 '- 1/2 cup and 2 tablespoons cocoa powder', '- 1 teaspoon baking soda','- 2 teaspoons espresso powder',
                                 '- 1 cup chocolate chips','- 8 ounces of white chocolate', '- 3 crushed candy canes'],
                'instructions' : ['1. In a bowl using a mixer fitted with a paddle attachment, beat the butter,'
                                  ' granulated sugar, and brown sugar until creamed.\n',
                                  '2. Then, mix in the egg, vanilla extract, and peppermint extract until combined.\n',
                                  '3. In a separate bowl, whisk all-purpose flour, cocoa powder, baking soda, and espresso powder until combined.\n',
                                  '4. With the mixer on low speed, pour the dry ingredients into the wet '
                                  'ingredients. Mix until combined, and then add the chocolate chips.\n',
                                  '5. Cover the dough tightly and chill in the refrigerator for 2 hours.\n',
                                  '6. Preheat the oven to 350 degrees fahrenheit. Scoop and roll dough,'
                                  ' 1.5 tablespoons each, into balls. Place onto baking sheet, and bake for '
                                  '11-12 minutes or until the edges appear set.\n',
                                  '7. Cool cookies for 5 minutes on the baking sheet and then move to a'
                                  ' cooling rack to cool completely. While cooling, melt the white chocolate in the microwave until smooth.\n',
                                  '8. Dip each cookie halfway into the white chocolate and '
                                  'sprinkle crushed candy canes on top of the chocolate for each cookie.\n']

            }
        }
    def getChocolateChips(self):
        return 'Chocolate Chip Cookies'
    def getSnickerdoodles(self):
        return 'Snickerdoodles'
    def getRedVelvet(self):
        return 'Red Velvet Cookies'
    def getShortbread(self):
        return 'Shortbread Cookies'
    def getCookieBars(self):
        return 'Sugar Cookie Bars'
    def getPBCookies(self):
        return 'Peanut Butter Cup Cookies'
    def getCrinkleCookies(self):
        return 'Chocolate Crinkle Cookies'
    def getPumpkinOatCookies(self):
        return 'Pumpkin Oatmeal Cookies'
    def getCookiesAndCream(self):
        return 'Cookies and Cream Cookies'
    def getPeppermintMochaCookies(self):
        return 'Peppermint Mocha Cookies'
    #getter methods

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeBookApp(root)
    root.mainloop()