<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="sss"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 11:12:18 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMDo0MzozNyBQTTsyNjY3"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMToxMjoxOCBQTTs4OzI3Nzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, qty" type="Integer" array="False" size=""/>
            <declare name="coffeeprice" type="Real" array="False" size=""/>
            <declare name="qtycoffee" type="Real" array="False" size=""/>
            <assign variable="qtycoffee" expression="10"/>
            <assign variable="coffeeprice" expression="25"/>
            <declare name="teaprice" type="Real" array="False" size=""/>
            <declare name="qtytea" type="Real" array="False" size=""/>
            <assign variable="qtytea" expression="0"/>
            <assign variable="teaprice" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - &quot;&amp;coffeeprice&amp; &quot; Baht - Qty: &quot; &amp;qtycoffee" newline="True"/>
            <output expression="&quot;2. Tea - &quot;&amp;teaprice&amp; &quot; Baht - Qty: &quot; &amp;qtytea" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="qty"/>
                    <if expression="qty&lt;=qtycoffee">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;coffeeprice*qty&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="qty"/>
                    <if expression="qty&lt;=qtytea">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp;teaprice*qty&amp; &quot; Baht&quot;" newline="True"/>
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