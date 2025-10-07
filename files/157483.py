<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="PC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 10:00:09 PM"/>
        <attribute name="created" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MDk6MDc6NTkgUE07MjUwMQ=="/>
        <attribute name="edited" value="UEM7REVTS1RPUC03Q0U2R0tEOzI1NjgtMDctMTk7MTA6MDA6MDkgUE07NTsyNTkz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <declare name="Coffee, CoffeeQty, Tea, TeaQty, quantity, total" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="25"/>
            <assign variable="Tea" expression="20"/>
            <assign variable="CoffeeQty" expression="10"/>
            <assign variable="TeaQty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1.Coffee -&quot;&amp;Coffee&amp;&quot;Baht-Qty:&quot;&amp;CoffeeQty" newline="True"/>
            <output expression="&quot;2.Tea -&quot;&amp;Tea&amp;&quot;Baht-Qty:&quot;&amp;TeaQty" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu=1">
                <then>
                    <if expression="quantity&lt;=CoffeeQty">
                        <then>
                            <assign variable="total" expression="Coffee*quantity"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu=2">
                        <then>
                            <if expression="quantity&lt;=TeaQty">
                                <then>
                                    <assign variable="total" expression="Tea*quantity"/>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
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