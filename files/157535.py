<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 08:57:14 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0xOTswNzozMjozOCBQTTsyNzU3"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0yMDswODo1NzoxNCBQTTs5OzI4Njc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, coffeePrice, teaPrice, coffeeQty, teaQty, totalPrice, orderQty" type="Integer" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="orderQty"/>
            <if expression="menu==1">
                <then>
                    <if expression="orderQty&lt;=coffeeQty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="totalPrice" expression="coffeePrice * orderQty"/>
                            <output expression="&quot;Total Price: &quot;&amp;totalPrice&amp;&quot; Baht&quot;" newline="True"/>
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
                            <if expression="orderQty&lt;=teaQty">
                                <then>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <assign variable="totalPrice" expression="teaPrice * orderQty"/>
                                    <output expression="&quot;Total Price: &quot;&amp;totalPrice&amp;&quot; Baht&quot;" newline="True"/>
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