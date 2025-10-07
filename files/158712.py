<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:05:43 PM"/>
        <attribute name="created" value="QWRtaW47TEFQVE9QLVYyVDE1UFE3OzI1NjgtMDctMjI7MDg6NTA6NTkgUE07MjgzOQ=="/>
        <attribute name="edited" value="QWRtaW47TEFQVE9QLVYyVDE1UFE3OzI1NjgtMDctMjI7MDk6MDU6NDMgUE07MTsyOTQx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, newMoney" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="Money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + interest / 100)"/>
                <output expression="&quot;Year &quot; &amp; year &amp; &quot;: &quot;&amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>