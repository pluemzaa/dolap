<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="l2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:33:37 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MDM6MzEgUE07MjU3Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzM6MzcgUE07NjsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffeeQty, teaQty, menu, qty" type="Integer" array="False" size=""/>
            <declare name="coffeePrice, teaPrice" type="Real" array="False" size=""/>
            <assign variable="coffeePrice" expression="25"/>
            <assign variable="teaPrice" expression="20"/>
            <assign variable="coffeeQty" expression="10"/>
            <assign variable="teaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot;&amp;coffeePrice&amp;&quot; Baht - Qty: &quot;&amp;coffeeQty" newline="True"/>
            <output expression="&quot;2. Tea - &quot;&amp;teaPrice&amp;&quot; Baht - Qty: &quot; &amp; teaQty" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qty"/>
            <if expression="menu==1">
                <then>
                    <comment text="Coffee"/>
                    <if expression="coffeeQty &gt;= qty">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;(coffeePrice*qty)&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <comment text="Tea"/>
                    <if expression="menu==2">
                        <then>
                            <if expression="teaQty &gt;= qty">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot;&amp;(teaPrice * qty) &amp;&quot; Baht&quot;" newline="True"/>
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