<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.2 flowchart"/>
        <attribute name="authors" value="Windows11"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 07:26:00 PM"/>
        <attribute name="created" value="V2luZG93czExO01TSTsyNTY4LTA3LTE2OzA2OjM3OjU4IFBNOzIzODY="/>
        <attribute name="edited" value="V2luZG93czExO01TSTsyNTY4LTA3LTE2OzA3OjI2OjAwIFBNOzc7MjQ4Ng=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="select, coffeePrice, teaPrice, quantity, total, coffeeQty, teaQty" type="Real" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="select"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="select==1">
                <then>
                    <if expression="quantity&lt;=coffeeQty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="quantity*coffeePrice"/>
                            <output expression="&quot;Total Price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="select==2">
                        <then>
                            <if expression="quantity&lt;=teaQty">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="quantity*teaPrice"/>
                                    <output expression="&quot;Total Price &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>