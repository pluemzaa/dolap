<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lap2.1"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 12:27:22 AM"/>
        <attribute name="created" value="SFA7TEFQVE9QLUhROTVETlROOzI1NjgtMDctMjE7MDk6Mzk6MDMgUE07MjUzMQ=="/>
        <attribute name="edited" value="SFA7TEFQVE9QLUhROTVETlROOzI1NjgtMDctMjI7MTI6Mjc6MjIgQU07MzsyNjE5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="name" type="String" array="True" size="2"/>
            <declare name="price" type="Integer" array="True" size="2"/>
            <declare name="quantity" type="Integer" array="True" size="2"/>
            <declare name="total, menu, order" type="Integer" array="False" size=""/>
            <assign variable="name[0]" expression="&quot;Coffee &quot;"/>
            <assign variable="name[1]" expression="&quot;Tea &quot;"/>
            <assign variable="price[0]" expression="25"/>
            <assign variable="price[1]" expression="20"/>
            <assign variable="quantity[0]" expression="10"/>
            <assign variable="quantity[1]" expression="0"/>
            <output expression="&quot; Coffee&quot;" newline="True"/>
            <output expression="&quot;Tea&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="order"/>
            <if expression="order&gt;quantity[menu-1]">
                <then>
                    <output expression="&quot;Sorry,&quot;&amp; name[menu-1]&amp;&quot;out of stock&quot;" newline="True"/>
                </then>
                <else>
                    <assign variable="total" expression="order*price[menu-1]"/>
                    <output expression="&quot;You purchased&quot;&amp; name[menu-1]" newline="True"/>
                    <output expression="&quot;TOtalPrice.&quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>