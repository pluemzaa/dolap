<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab 2"/>
        <attribute name="authors" value="DELL"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 05:33:24 PM"/>
        <attribute name="created" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNDo0MDoxNyBQTTsyNjU3"/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNTozMzoyNCBQTTszOzI3Njg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, coffeeQty, teaPrice, teaQty, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaQty" expression="0"/>
            <assign variable="teaPrice" expression="20"/>
            <output expression="&quot; Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1.Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2.Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="coffeePrice*quantity"/>
                            <output expression="&quot;Total Price:&quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="quantity"/>
                    <if expression="quantity==0">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <assign variable="total" expression="teaPrice*quantity"/>
                            <output expression="&quot;Total Price:&quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>