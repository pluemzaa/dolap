<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Rabbit Vender"/>
        <attribute name="authors" value="prabb"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-23 11:45:26 PM"/>
        <attribute name="created" value="cHJhYmI7REVTS1RPUC1WQjZCODY4OzI1NjgtMDctMTY7MDM6NTA6MzcgUE07MjgzNw=="/>
        <attribute name="edited" value="cHJhYmI7REVTS1RPUC1WQjZCODY4OzI1NjgtMDctMTY7MDQ6MjU6NTAgUE07NzsyOTQ5"/>
        <attribute name="edited" value="SUM7TkItSUM7MjU2OC0wNy0yMzsxMTo0NToyNiBQTTsxOzE4NzM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, total, coffeeQty, teaQty, coffeePrice, teaPrice" type="Real" array="False" size=""/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <assign variable="coffeePrice" expression="25"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <assign variable="teaPrice" expression="20"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu = 1">
                <then>
                    <if expression="coffeeQty &gt;= quantity">
                        <then>
                            <assign variable="total" expression="quantity*coffeePrice"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu = 2">
                        <then>
                            <if expression="teaQty &gt; quantity">
                                <then>
                                    <assign variable="total" expression="quantity*teaPrice"/>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;invalid menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>