<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work2lab4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:47:29 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MTk6NTkgUE07MjU4OQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDc6MjkgUE07MjsyNjk2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, menu, quantity" type="Real" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="10"/>
            <assign variable="Tea" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu==1">
                <then>
                    <if expression="Coffee &gt;= quantity">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="quantity * 25"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
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
                            <if expression="Tea &gt;= quantity">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="quantity * 20"/>
                                    <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
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