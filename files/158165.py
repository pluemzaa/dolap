<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 09:56:25 PM"/>
        <attribute name="created" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMjE7MDk6MTI6MjEgUE07MjIxOA=="/>
        <attribute name="edited" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMjE7MDk6NTY6MjUgUE07MTsyMzM4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, per, year, temp, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="per"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i&lt;year+1">
                <assign variable="temp" expression="money*(1+(per/100))"/>
                <assign variable="money" expression="temp"/>
                <output expression="&quot;Year&quot;&amp;i&amp;&quot;: &quot;&amp;Tofixed(money,2)" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>