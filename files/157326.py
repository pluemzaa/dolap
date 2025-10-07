<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:15:14 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozMTo0NyBQTTsyNTQ3"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozNjoxNyBQTTsxO2NvbXB1dGVyO0NQQ09NOzI1NjgtMDctMTc7MDI6NTU6MzggUE07NTI2OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswNDoxNToxNCBQTTs3OzI2NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeePrice, teaPrice" type="Integer" array="False" size=""/>
            <declare name="coffeeQty, teaQty" type="Integer" array="False" size=""/>
            <declare name="teaquantity, coffeequantity" type="Integer" array="False" size=""/>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="Tea" type="Integer" array="False" size=""/>
            <declare name="Cofee" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <assign variable="coffeeQty" expression="10"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: &quot;&amp;coffeeQty" newline="True"/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: &quot;&amp;teaQty" newline="True"/>
            <assign variable="teaPrice" expression="20"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="coffeequantity"/>
                    <if expression="coffeequantity &lt;= coffeeQty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="coffeequantity*coffeePrice"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="teaquantity"/>
                            <if expression="teaquantity &lt; teaQty">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="teaPrice*teaquantity"/>
                                    <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Invaild menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>