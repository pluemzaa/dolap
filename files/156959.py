<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test1_lab5"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:57:24 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDE6MjM6MDMgUE07MjU3MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTc6MjQgUE07NjsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Total, Coffee, Tea, n, CoffeeQTT, TeaQTT" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="n"/>
            <if expression="n=1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="CoffeeQTT"/>
                    <if expression="CoffeeQTT&lt;=10">
                        <then>
                            <if expression="CoffeeQTT&lt;=0">
                                <then>
                                    <output expression="&quot;Enter your quantity again&quot;" newline="True"/>
                                </then>
                                <else/>
                            </if>
                            <assign variable="Total" expression="Coffee * CoffeeQTT"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; Total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="n=2">
                        <then>
                            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                            <input variable="TeaQTT"/>
                            <if expression="TeaQTT&lt;=10">
                                <then/>
                                <else>
                                    <output expression="&quot;Error&quot;" newline="True"/>
                                </else>
                            </if>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Error&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>