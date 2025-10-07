<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4"/>
        <attribute name="authors" value="Henry"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 09:57:56 PM"/>
        <attribute name="created" value="SGVucnk7REVTS1RPUC1QQUtPMzNJOzIwMjUtMDctMjA7MDk6MzU6MTcgUE07Mjg2Mg=="/>
        <attribute name="edited" value="SGVucnk7REVTS1RPUC1QQUtPMzNJOzIwMjUtMDctMjA7MDk6NTc6NTYgUE07MTsyOTc3"/>
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
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;Tofixed(money,2)" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>