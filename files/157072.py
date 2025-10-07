<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="tor moo bu sha"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:54:52 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MDA6MzggUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTQ6MzcgUE07MTA7Mjc0MA=="/>
        <attribute name="edited" value="cHVrYW47REVTS1RPUC0yQ04zQTM2OzIwMjUtMDctMTY7MDY6NTQ6NTIgUE07NDsyOTQy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, quantity, total, item" type="Integer" array="False" size=""/>
            <declare name="itemdata" type="String" array="False" size=""/>
            <assign variable="item" expression="0"/>
            <assign variable="Coffee" expression="10"/>
            <assign variable="Tea" expression="0"/>
            <output expression="&quot;Beverage List:&quot;&amp;&#13;&#10;tochar(13)&amp;&quot;1. Coffee - 25 Baht - Qty: &quot; &amp;(Coffee)&#13;&#10;&amp;tochar(13)&amp;&quot;2. Tea - 20 Baht - Qty: &quot; &amp; (Tea)" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="item"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="item == 1">
                <then>
                    <assign variable="itemdata" expression="&quot;Coffee&quot;"/>
                    <if expression="quantity &lt;= Coffee">
                        <then>
                            <assign variable="total" expression="(quantity * 25)"/>
                            <output expression="&quot;You purchased &quot; &amp;(itemdata)  &#13;&#10;&amp; tochar(13) &amp;&quot;Total Price : &quot; &amp; (total) &amp; &quot; Baht&quot;&#13;&#10;&amp; tochar(13) &amp;&quot;Enjoy!&quot;" newline="False"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry,&quot;&amp;(itemdata)&amp;&quot; out of stock&quot;" newline="False"/>
                        </else>
                    </if>
                </then>
                <else>
                    <assign variable="itemdata" expression="&quot;Tea&quot;"/>
                    <if expression="quantity &lt;= Tea">
                        <then>
                            <assign variable="total" expression="(quantity * 20)"/>
                            <output expression="&quot;You purchased &quot; &amp; (itemdata) &#13;&#10;&amp; tochar(13) &amp;&quot;Total Price : &quot; &amp; (total) &amp; &quot; Baht&quot;&#13;&#10;&amp; tochar(13) &amp;&quot;Enjoy!&quot;" newline="False"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry,&quot;&amp;(itemdata)&amp;&quot; out of stock&quot;" newline="False"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>