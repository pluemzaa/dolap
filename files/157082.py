<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 12:49:10 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0xNjswNDoyMDoyOCBQTTsyNzUy"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0xNzsxMjo0OToxMCBBTTs4OzI4NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num, s1, e1, coffeePrice, coffeeQty, teaPrice, teaQty, s2, e2, total" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="num"/>
            <if expression="num == 2">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="e1"/>
                    <if expression="e1 == teaQty">
                        <then/>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="num == 1">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="e2"/>
                            <if expression="e2 &lt;= coffeeQty">
                                <then>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <assign variable="total" expression="e2 * coffeePrice"/>
                                    <output expression="&quot;Total Price:&quot; &amp; total &amp; &quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
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