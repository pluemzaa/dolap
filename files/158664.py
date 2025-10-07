<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flow&#3586;&#3657;&#3629;2"/>
        <attribute name="authors" value="nitip"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 05:30:42 PM"/>
        <attribute name="created" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6MTE6NDIgUE07MjA3MA=="/>
        <attribute name="edited" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6MzA6NDIgUE07NDsyMTgy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, totalPriceCoffee, totalPriceTea" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot; 1. Coffee - 25 Baht - Qty: 10 &quot;" newline="True"/>
            <output expression="&quot; 2. Tea - 20 Baht - Qty: 0 &quot;" newline="True"/>
            <output expression="&quot; Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot; Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu == 1">
                <then>
                    <if expression="quantity &lt;= 10">
                        <then>
                            <assign variable="totalPriceCoffee" expression="quantity * 25"/>
                            <output expression="&quot; You purchased Coffee &quot;" newline="True"/>
                            <output expression="&quot;Enter Price:&quot; &amp; totalPriceCoffee &amp; &quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <if expression="quantity &gt; 0">
                                <then>
                                    <output expression="&quot; Sorry, tea out of stock &quot;" newline="True"/>
                                </then>
                                <else/>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>