<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="labf2"/>
        <attribute name="authors" value="Legion"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 09:11:49 PM"/>
        <attribute name="created" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTE2OzA1OjI2OjMzIFBNOzI5NzI="/>
        <attribute name="edited" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTIwOzA5OjExOjQ5IFBNOzI7MzA4MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, total" type="Integer" array="False" size=""/>
            <declare name="CoffeeQty, TeaQty, price" type="Real" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <assign variable="CoffeeQty" expression="10"/>
            <assign variable="TeaQty" expression="0"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: &quot; &amp; (CoffeeQty)" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty : &quot;&amp; (TeaQty)" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu == 1">
                <then>
                    <if expression="quantity&gt;coffeeQty">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="price" expression="25"/>
                            <assign variable="total" expression="price*quantity"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;(total )&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else/>
            </if>
            <if expression="menu==2">
                <then>
                    <if expression="quantity&gt;TeaQty">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="price" expression="20"/>
                            <assign variable="total" expression="price*quantity"/>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; (total) &amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else/>
            </if>
        </body>
    </function>
</flowgorithm>